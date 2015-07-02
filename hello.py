import random
import sys
import os

print("Hello world")
name="Lakhan"
print(name)
print(5**2)
print("\"This is quote\"")

list=["lakhan",1,3,"4"]
print(list[0])
print(list[0:3])
print(list)

tp=(13,4,1,45)
print(tp);

age=21
if age > 18 :
    print("you can marry!")
elif age < 18 :
    print("aha you can marry!")
else :
    print("you can always marry")

'''
logical operators are:
and or not
if((age > 18) and (age <= 21)):
    print("you are mature")
'''
# for loop

'''
for x in range(0,10):
    print(x," ",end="")
print("\n")
for y in list:
    print(y)
for z in [2,3,5,76,10]:
    print(z)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for m in range(0,len(matrix)):
    for n in range(0,len(matrix[0])):
        print(matrix[m][n])

'''

#while loop
'''
random_num=random.randrange(0,100)
while(random_num!=15):
    print(random_num)
    random_num=random.randrange(0,100)
'''

'''
function and things you can do with list
len(list)
max(list)
min(list)
list.sort()
list.reverse()
del list[1]
list.append("avc")
list.insert(1,"abc")
list.remove("abc")
list2=[1,2,3]
list3=list+list2
list3=[list,list2]

'''

'''
Tuple and things that can be done with Tuple

it has fixed set of values, this set can not be chaged, you can convert this into list and can den manipulate it
tp1=(1,2,3)
list=list(tp1)
list.append(5)
tp2=tuple(list)
len(tp2)
min(tp2)
max(tp2)


'''

'''
Dictionaries and things that can be done with them
we cannot append Dictionaries with + sign
villans={"Haider":"Salman","Tevar":"Arjun"}
print("Tevar") // will display the value of this key
it stores in key value form
del villans["Tevar"]
len(villans);
villans.get("tevaar")
villans.keys()
villans.values()
'''

'''
Conditions
if else elif == != > >= < <=
'''
# Commnet

'''
Mulitline comment

Data types in python
Numbers, Strings, Lists, Tuples, Dictionaries(Map)
+
-
*
/
%
** exponential 5**2
// floor value
'''
