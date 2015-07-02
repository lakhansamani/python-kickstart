import sys
import os

long_st="hello world"
print(long_st[0:4])
print(long_st[-3:]) #last 3 char
print(long_st[:-3]) #upto last 3 char
print(long_st[:-6]+" lakhan ") #addin to string
#formating string is similar to c
print("%c"%"X")

print(long_st.capitalize())
print(long_st.find("wor"))
print(long_st.isalpha())
print(long_st.isalnum())
print(len(long_st))
print(long_st.replace("world","lakhan"))
print(long_st.strip())

split_str=long_st.split(" ")
print(split_str)
