i=1
while i<=10 :
    print("This is the "+str(i)+" th iteration")
    i+=1
# lets learn about the freaking FOR loop
for letter in " Kaif's Academy " :
    print(letter)
# Range function
for index in range(1,11,2) :
    print(index)
# We can use For loop in Python to loop through like any collection we have
# Exponent Functions in  Python USER MADE
def raise_to_power(base,exp) :
    result=1
    for i in range(exp) :
        result=result*base
    return result

print(raise_to_power(5,4))
