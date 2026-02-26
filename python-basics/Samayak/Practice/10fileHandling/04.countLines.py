# 4. Count Lines in a File: Write a program that counts the number of lines in myfile.txt and prints the count.

with open('myfile.txt', 'r') as file:
    lin = file.readlines()
    print(len(lin))
    