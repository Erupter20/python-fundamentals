'''
Project: Hotel Booking System
Goal:
Create a program that allows users to:
•View available rooms
•Book a room
•Cancel a booking
•View all bookings
•Exit the system
'''

print("Welcome to Hotel Booking System\n")

rooms = {
    101: {"Type": "Single", "Price": 1800, "booked": False},
    102: {"Type": "Double","Price":3200,"booked": True},
    103: {"Type": "Single", "Price": 1800, "booked": False},
    104: {"Type": "Double","Price":3200,"booked": True}
}

bookings = {}

while True:
    print("-----Console-----")
    print("1.View Available Rooms")
    print("2.Book a Room")
    print("3.Cancel a booking")
    print("4.View All Bookings")
    print("5.Exit the System")

    choice = input("Enter your choice(1 - 5):\n")
    if choice == "1":
        print("1.Available Rooms:\n")
        for room_no , info in rooms.items():
            if not info["booked"]:
                print(f"Room: {room_no} - {info['Type']} - INR{info['Price']}")
    elif choice== "2":
        room_no = int(input("Enter room number to book: "))
        if room_no in rooms:
            if not rooms[room_no]["booked"]:
                name = input("Enter your name: ")
                days = int(input("Enter number of days: "))
                total = rooms[room_no]["Price"] * days
                rooms[room_no]["booked"] = True
                bookings[room_no] = {"Name": name, "Days": days, "Total": total}
                print(f"Room {room_no} booked successfully for {name}!")
                print(f"Total Bill: ₹{total}")
            else:
                print("Room already booked!")
        else:
            print("Invalid room number!")
    elif choice == "3":
        print("3.Cancel a booking\n")
        room_no = int(input("Enter room number to cancel: "))
        if room_no in bookings:
            rooms[room_no]["booked"] = False
            del bookings[room_no]
            print(f"Booking for room {room_no} canceled sucessfully!")
        else:
            print("No booking found for that room!")
    elif choice == "4":
        if len(bookings) == 0:
            print("No current bookings!")
        else:
            print("\nCurrent bookings:")
            for room_no, details in bookings.items():
                print(f"Room {room_no} → {details['Name']} | Days: {details['Days']} | ₹{details['Total']}")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice, try again\n")