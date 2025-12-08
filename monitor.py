
import requests
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
    # test with a fake url that returns 404
    check_website("https://httpbin.org/status/404")

    # test with google because its always online
    check_website("https://www.google.com") 

