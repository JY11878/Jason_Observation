'''
9.	Write a program to calculate average using sentinel loop.
Output:

Enter a number ( to quit) >> 34
Enter a number ( to quit) >> 23
Enter a number ( to quit) >> 0
Enter a number ( to quit) >> -25
Enter a number ( to quit) >> -34.4
Enter a number ( to quit) >> 22.7
Enter a number ( to quit) >>

The average of the numbers is 3.38333333333
'''

numbers = []
while True:
    num = input("Enter a number ( to quit):")
    if num == "":
        break
    numbers.append(float(num))
avg = sum(numbers) / len(numbers)
print("The average of the numbers is", avg)