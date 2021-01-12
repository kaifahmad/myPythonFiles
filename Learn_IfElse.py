# We will learn If else syntax here
is_male=True
is_tall=True


#If statements and comparison
    def max_num(num1, num2, num3):

        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3

print(max_num(200,5,15))


