"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When you put anything besides a number.
2. When will a ZeroDivisionError occur?
If the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
No
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")