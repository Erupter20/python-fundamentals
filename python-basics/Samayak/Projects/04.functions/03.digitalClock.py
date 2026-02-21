# 03. Show the current time updating every second using a user-defined function.

import time 
from datetime import datetime

# Function to display current time

def show_time():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current Time:", current_time, end = "\r")
        time.sleep(1)

show_time()