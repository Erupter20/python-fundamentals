# 15. Write a program that displays message based on traffic light color.

light = input("enter color of light:\n")
light = light.lower()
if light == "red":
    print("STOP")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("GO")
else:
    print("Invalid input")