import sys
import os

class Person:
    __name="" ##__ means private
    __age=0

    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_age(self, age):
        self.__age=age
    def get_age(self):
        return self.__age
    #constructor

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_type(self):
        print("Person")

    def toString(self):
        return "{}\'s age is {}".format(self.__name,self.__age)

lakhan = Person("lakhan",21)
print(lakhan.toString())
