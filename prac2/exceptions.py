try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# value error occurs if a string is enter instead of an integer
# zero division error occurs when the denominator is 0
# a loop could be added that will continue to prompt the user until a number other than 0 is chosen for the denomimator
