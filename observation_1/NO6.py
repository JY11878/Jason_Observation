'''
6.	The speeding ticket fine policy in Podunksville
is $50 plus $5 for each mph over the limit plus a
penalty of $200 for any speed over 90 mph. Write a
program that accepts a speed limit and a clocked speed
and either prints a message indicating the speed was legal
or prints the amount of the fine, if the speed is illegal.
'''

limit = float(input("Enter the speed limit in mph"))
speed = float(input("Enter your speed in mph"))
if speed <= limit:
    print("Speed is legal")
elif speed <= 90:
    fine = 50 + 5 * (speed - limit)
    print("Fine amount:", fine)
else:
    fine = 50 + 5 * (speed - limit) + 200
    print("Fine amount:", fine)