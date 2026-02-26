import time  # Import time module

# Ask user for countdown time in seconds
seconds = int(input("Enter countdown time in seconds: "))

# Countdown loop
while seconds > 0:
    print(seconds)      # Show remaining seconds
    time.sleep(1)       # Wait 1 second
    seconds -= 1        # Decrease seconds by 1

print("⏰ Time's up!")   # When countdown ends
