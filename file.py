import sys
import os

#create or open file
tf=open('text.txt','wb')
print(tf.mode)
print(tf.name)
tf.write(bytes("writing into file\n","UTF-8"))
tf.close()
txt=open("text.txt","r+")
#r+ read and write mode
text=txt.read()
print(text)
os.remove("text.txt")
