# 6. Read and Print Specific Lines: Write a program that reads myfile.txt and prints only the first two lines.

with open ('myfile.txt' , 'r') as file:
    content  = file.readlines()[:2]
for line in content:
    print(line.strip())
