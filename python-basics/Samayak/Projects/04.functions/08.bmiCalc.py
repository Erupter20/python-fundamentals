# Calculate a person’s BMI and tell whether they are Underweight, Normal, Overweight, or Obese using functions.

def calculate_bmi(weight, height):
    bmi = weight/(height ** 2)
    return bmi

# Function to return bmi category:

def bmi_category(bmi):

    if bmi < 18.5:
        print("Underweight")
    elif 18.8<= bmi <25:
        print("Normal")
    else:
        print("overweight")

# Function to display result
def show_bmi_result(name, weight, height):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    print("\n------ BMI REPORT ------")
    print(f"Name: {name}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("------------------------")


# Main program
name = input("Enter your name: ")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))


show_bmi_result(name, weight, height)