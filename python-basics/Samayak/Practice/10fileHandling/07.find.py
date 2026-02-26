# 7. Find : Write a program that searches for a specific word in myfile.txt

with open ('myfile.txt' ,'r') as file:
    content = file.read()

word_to_find = "exercise"

with open ('myfile.txt' ,'r') as f:
    if word_to_find in f.read():
        print(f"{word_to_find} was found\n")
    else:
        print(f"{word_to_find} isn't present\n")