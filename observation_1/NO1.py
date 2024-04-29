#1.	Write a program to open a file and read data from it then display it on the console.

file = open("text_1", "r")
text = file.read()
print(text)