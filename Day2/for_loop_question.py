"""
Take a string input from user.
Find the sum of all the nos. in the string and print the final sum.
"""


number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

