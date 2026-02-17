# Write a program to convert temperature from Celsius to Fahrenheit or vice versa.

temp = int(input("Enter temp :\n"))
scale = input("enter scale(C/F):\n")
scale = scale.upper()

if scale == "C":
    converted_temp = (temp * 9/5) + 32
    print(f"{converted_temp} degrees Fahrenheit")
elif scale == "F":
    converted_temp = (temp - 32) * 5/9
    print(f"{converted_temp} degrees celcius")
print(converted_temp)