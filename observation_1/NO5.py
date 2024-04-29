#5.	Write a program to find the maximum of a series of numbers using python function.
n = int(input("How many numbers do you want"))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter a number: ")))

a = max(numbers)
print("the max number is", a)