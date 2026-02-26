# 5. Copy File Content: Write a program that copies the content of myfile.txt to a new file called copyfile.txt. 

with open('myfile.txt', 'r') as file:
    toCopy = file.read()

with open('copied.txt', 'w') as file:
    file.write(toCopy)
    content = file.write()
    
with open('copied.txt', 'r') as file:
    cont = file.read(toCopy)
    print(cont)