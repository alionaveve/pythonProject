#Write a program that uses a while loop to calculate the factorial
# of a given positive integer n.
# The factorial of a number is the product of all positive integers from 1 to n.

num = int(input("Enter  the number"))
factorial = 1

if num < 0:
   print("mustl be positive")
elif num == 0:
   print("factorial = 1")
else:
    while num > 1:
        factorial = factorial * num
        num = num - 1
print(num, factorial)