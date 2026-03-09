# 09. String Reversal: Write a program that takes a string and prints it in reverse order using a loop.

s = "hello world"

for i in range(len(s)-1, -1, -1):
    print(s[i])