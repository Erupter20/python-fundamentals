# 2. Read a Text File: Write a program that opens myfile.txt (from the previous question), reads its content, and prints it to the console.


with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)