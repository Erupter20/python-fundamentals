# 10. Tast: Write a Python program that creates a file named my_notes.txt, writes "This is my first note!" into it, and then reads the content of the file to print it.

file = open('my_notes.txt' ,'w')
file.write("This is my first note!")

file = open('my_notes.txt', 'r')
content = file.read()

print(content)