# 12.Write a Python program to calculate Body Mass Index (BMI).

weight = int(input("Enter your weight:\n"))
height = int(input("Enter your height:\n"))

bmi = weight/(height**2)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif 18.8<= bmi <25:
    print("Normal")
else:
    print("overweight")
