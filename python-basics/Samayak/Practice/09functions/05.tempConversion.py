# 5. Temperature Conversion: Write a function named celsius_to_fahrenheit that converts a temperature from Celsius to Fahrenheit.

def tempConversion(a, scale):
    if scale == "C":
        converted_temp = (a * 9/5) + 32
        return converted_temp
    elif scale == "F":
        converted_temp = (a - 32) * 5/9
        return converted_temp
    return converted_temp
print(tempConversion(40, "C"))