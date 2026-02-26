# 3. Append to a File: Modify your program to append the text "This is a file handling exercise." to myfile.txt.

with open('myfile.txt', 'w') as file:
    content = file.write("\n This is a file handling exercise.")

with open('myfile.txt', 'r') as file:
    rea = file.read()
    print(rea)