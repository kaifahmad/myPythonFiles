#color=input("Enter your color")
#plural_noun=input("Enter your plural noun")
#celebrity=input("Enter your celebrity")
#print("Roses are "+color)
#print(plural_noun+" are+ blue")
#print("I love "+celebrity)
# Now we are going to learn to make a LIST
family= ["Kaif","Saif","Tanvir","Humaira","Zubaida"]
print(family[-1])# allows negative indexing
print(family[1:3])
#can be modified using assignment operation
print(family)
lucky_nos=[2,3,5,7,11,13,17,19]
#family.extend(lucky_nos)
# Clearly We can append values to a list
print(family)
family.append("Creed")
print(family)
family.insert(1,"Shahab") #Appending at demand
print(family)
family.remove("Shahab")
print(family)
#family.remove(2)
print(family)
#family.clear()
#print(family)
family.pop()

print(family)
print(family.index("Zubaida"))
print(family.count("Tanvir")) #Counts the number of times Tanvir occurs in the List
print("We are here")
family.sort() #Here we can sort all the elements of the LIST
# Lets sort the lucky_nos
print(family)
print(lucky_nos)
lucky_nos.sort()
lucky_nos.reverse() #reverses the Order
print(lucky_nos)
family1=family.copy() #Copy of the the existing Family list
