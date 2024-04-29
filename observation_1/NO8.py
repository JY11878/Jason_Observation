'''
8.	Write a program to calculate average using interactive  loops.
Output:

Enter a number >> 32
Do you have more numbers (yes or no)? yes
Enter a number >> 45
Do you have more numbers (yes or no)? y
Enter a number >> 34
Do you have more numbers (yes or no)? y
Enter a number >> 76
Do you have more numbers (yes or no)? y
Enter a number >> 45
Do you have more numbers (yes or no)? nope
The average of the numbers is 46.4
'''
numbers = []
while True:
    num = input("Enter a number >> ")
    numbers.append(float(num))
    more = input("Do you have more numbers (yes or no)? ")
    if more.lower() != "yes" and more.lower() != "y":
        break
avg = sum(numbers) / len(numbers)
print("The average of the numbers is", avg)
