
import requests
import time
from datetime import datetime
import sqlite3
import json
import os



DB_PATH = "monitoring.db"

def init_db(db_path: str = DB_PATH):
    """initialize the SQLite database and create table if not exists"""
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS checks (
                    timestamp TEXT,
                    url TEXT,
                    status_code INTEGER,
                    response_time_ms REAL
                )
            ''')
            
    except Exception as e:
        print(f"Error initializing DB: {e}")



def save_to_db(now: str, url: str, status_code: int, response_time: float, db_path: str = DB_PATH):
    """save the status result to the database"""
    try:
        with sqlite3.connect(db_path) as conn:
            
            conn.execute('''
                INSERT INTO checks (timestamp, url, status_code, response_time_ms)
                VALUES (?, ?, ?, ?)
            ''', (now, url, status_code, response_time))
            
    except Exception as e:
        print(f"Database error: {e}")



def load_config(config_path: str = "config.json"):
    """load configuration from JSON file"""
    if not os.path.exists(config_path):
        print("Config file not found. Creating default config.")
        default_config = {
            "url": "https://www.google.com",
              "interval_seconds": 30
              }
        
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config
    
    with open(config_path, 'r') as f:
        return json.load(f)




def check_website(url: str, db_path: str = DB_PATH):
    """simple function to check the status of a website"""
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get current time for logging

    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # convert to milliseconds

        if response.status_code == 200:
            print(f"[{now}] Website {url} is online. Time: {response_time:.0f}ms")
        else:
            print(f"[{now}] Website {url} returned an error. Status: {response.status_code}")

        # save result to database
        save_to_db(now, url, response.status_code, response_time, db_path=db_path)

    except Exception as e:
        print(f"[{now}] Connection failed. Error: {e}")
        save_to_db(now, url, 0, 0.0, db_path=db_path)






if __name__ == "__main__":
    
    
    config = load_config()
    url = config.get("url")
    interval = config.get("interval_seconds", 10) # default 10 if not set

    print(f"\n Starting monitor for {url} ...")
    print(f" Interval: {interval} seconds")
    print("Press CTRL+C to stop.")

    # initialize database
    init_db(DB_PATH)

    try:
        # loop forever until user stops it
        while True:
            check_website(url)
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nMonitor stopped by user.")