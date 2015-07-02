import sys
import os

class person:
    __name=""
    __age=""
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def toString(self):
        return "{}'s age is {}".format(self.__name, self.__age);
    def set_name(self, name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_age(self, age):
        self.__age=age
    def get_age(self):
        return self.__age
class emp(person):
    __salary=0
    def __init__(self, name,age,salary):
        self.__salary=salary
        person.__init__(self,name,age)
    def toString(self):
        return "{}'s age is {}, and salary is {}".format(self.get_name(),self.get_age(),self.__salary);

e1=emp("lakhan",21,100000)
print(e1.toString())
