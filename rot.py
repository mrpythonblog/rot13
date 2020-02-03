#!/usr/bin/python3

print ("MrPython.blog.IR")

def rot13(text):
    trans = text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" , "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    text = text.translate(trans)
    return text

text = input("text : ")
text = rot13(text)
print(text)
