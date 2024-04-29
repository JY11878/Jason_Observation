#4.	Write a program to find the maximum of a series of numbers.
n = int(input("How many numbers do you want"))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter a number: ")))
    a = numbers[0]
    a = a+1
    for num in numbers:
        if num > a:
            a = num
print("the max number is", a)