import time  # Import time module

# Ask user for countdown time in seconds
seconds = int(input("Enter countdown time in seconds: "))

# Countdown loop
while seconds > 0:
    print(seconds)      
    time.sleep(1)       
    seconds -= 1       

print("Time's up!")   
