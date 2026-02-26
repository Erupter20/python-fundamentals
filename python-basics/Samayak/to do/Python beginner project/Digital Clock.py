from tkinter import *   # Import tkinter for GUI
import time             # Import time module to get current time

# Create the main window
root = Tk()
root.title("Digital Clock")     # Set window title
root.configure(bg="blue")       # Set background color to red

# Create a label to display time
label = Label(root, font=("Arial", 30), fg="white", bg="blue")  # White text on red background
label.pack(pady=40)  # Add some padding

# Function to update the time every second
def update():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS
    label.config(text=current_time)           # Update label with current time
    label.after(1000, update)                 # Call this function again after 1 second

update()  # Start the time update function

root.mainloop()  # Run the GUI loop
