# Python multithreading : make your code 10x faster (day 54)

import threading
import requests
import time


websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org",
    "https://www.stackoverflow.com"
]

# check if site is up or not
def check_website(url):
    try : 
        response = requests.get(url,timeout=5)
        print(f"{url} : status {response.status_code}")
    except Exception as e :
        print(f"{url} : Failed to connect..")

def run_slow():
    print("Starting sequential check..")
    start = time.perf_counter()

    for site in websites:
        check_website(site)
    end = time.perf_counter()
    print(f"Total time (slow) : {end-start:.2f} seconds \n")


def run_fast():
    print("Starting Multithreaded check..")

    start = time.perf_counter()
    threads = []

    for site in websites:
        thread = threading.Thread(target=check_website,args=(site,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end = time.perf_counter()
    print(f"Total time (fast) : {end-start:.2f} seconds \n")


# main function
if  __name__ == "__main__":
    run_slow()
    run_fast()