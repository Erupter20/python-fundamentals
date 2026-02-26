# . Replace Text : replaces(Q7) it with another word, saving the result in a new file called updatedfile.txt.


file = open("myfile.txt", 'r')
x = file.read()
x = x.replace("This", "That")    
