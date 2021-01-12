# Lets learn about exceptions
try:
    #value=10/0
    number = int(input("Enter a no. "))
    print(number)
    # catching specific exceptions is a good practice in python
except ValueError as err:
    print(err)
except ZeroDivisionError :
    print("Divided by zero")