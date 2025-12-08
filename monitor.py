
import requests
import time
from datetime import datetime


def check_website(url):
    """simple function to check the status of a website"""
    try:
        response = requests.get(url)

        # get current time for logging
        now = datetime.now().strftime("%H:%M:%S")

        if response.status_code == 200:
            print(f"[{now}] Website {url} is online. Status: {response.status_code}")
        else:
            print(f"[{now}] Website {url} returned an error. Status: {response.status_code}")

    except Exception as e:
        print(f"Connection failed. Error: {e}")




if __name__ == "__main__":
    
    # configuration
    url = "https://www.google.com" # test with google because its always online
    #url = "https://httpbin.org/status/404"  # test with a fake url that returns 404
    interval = 2  # check every x seconds


    print(f"\n Starting monitor for {url} ...")
    print("Press CTRL+C to stop.")

    try:
        # loop forever until user stops it
        while True:
            check_website(url)
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\nMonitor stopped by user.")