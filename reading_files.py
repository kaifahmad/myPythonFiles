# Open a file inside python
family_file= open("kaif.txt","r")
fam_file= open("Kaif.txt","a")
# r for read
# w for write
# a for append like add new info
# r+ for both reading and writing
#print(family_file.read())
# print all content
# print a specific line
print(family_file.readline()[2])
print(family_file.readline())
print(family_file.readline())
print(family_file.readable())
# appending DADI name
fam_file.write("\nZubaida - is my Dadi")
# Similarly w will try to overwrite the file and delete all the previous content using the same wtite command
# moves the cursor to the next line
family_file.close()



