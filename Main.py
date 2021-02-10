import math # Importing the Math Module.

a = int(input("Enter First Number: ")) # Taking first Number as the Input from User.
b = int(input("Enter Second Number: ")) # Taking Second Number as the Input from User.

'''In the Line-8 I have used the gcd function from the module for finding the HCF.
I have Even Used f string to Print results effectively.'''
print(f"The HCF of {a} and {b} is {math.gcd(a, b)}.") # Printing the Output.