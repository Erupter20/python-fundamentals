# 6. Write a class called Person with private attributes __name and __age, and methods to set and get these attributes.

name = input("Enter your name:\n")
age = int(input("enter your age:\n"))

class Person:
    def __init__(self, __name , __age):

        self.__name = name
        self.__age = age
        print (f"hello , {self.__name} aged {self.__age}")
        
