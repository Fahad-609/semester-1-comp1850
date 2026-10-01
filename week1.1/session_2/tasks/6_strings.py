# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") #all letters in the string are converted to lowercase
print(f"Modified String 2: {user_string.upper()}") #all letters in the string are converted to uppercase
print(f"Modified String 3: {user_string.strip()}") #removes leading and trailing whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces all occurrences of 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}") #converts the first character to uppercase and the rest to lowercase
print(f"Modified String 6: {user_string[::-1]}") #reverses the string
print(f"Modified String 7: {user_string.title()}") #converts the first character of each word to uppercase
print(f"Modified String 8: {len(user_string)}") #returns the length of the string
print(f"Modified String 9: {user_string.find('a')}")
print(f"Modified String 10: {user_string.count('a')}")
print(f"Modified String 11: {user_string.startswith('Hello')}")
print(f"Modified String 12: {user_string.endswith('!')}")
print(f"Modified String 13: {user_string.isalnum()}")
print(f"Modified String 14: {user_string.isalpha()}")#looks if its a letter
print(f"Modified String 15: {user_string.isdigit()}")#looks if its a digit



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!

message = "Hello, World!"
print( message.upper() )