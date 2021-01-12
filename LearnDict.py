# Learning Dictionaries in Python
# Convert 3 digit month name to full name
monthConversions= {"Jan": "January","Feb": "February","Mar": "March","Apr": "April"}
# Dictionaries should have a unique KEYS
print(monthConversions)
# Accessing a Dictionary
print(monthConversions["Jan"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Luv", "Not a valid Key"))
# Keys can be of any data Type
