
text = input("PLease enter a string:\n")
last_two_characters = text[-2:]
print(f"Last two characters in your entry is: {last_two_characters}")
length = len(text)
print(f"Your entry has: {length} characters")
print(f"The UPPERCASE value of the string you entered is: {text.upper()}")
print(f"The lowercase value of the string you entered is: {text.lower()}")
print(f"Are they equal? {text.lower()==text.upper()}")
index_of_a = text.find("a")
print(f"Index of character 'a' in your entry is: {index_of_a}")
text = text + " -cmpe113-"
print(f"The strings are concatenated: {text}")
new_length = len(text)
print(f"It's length becomes: {new_length}")
first_space = text.find(' ')
result = text[first_space-1]+text[first_space]+text[first_space+1]
print(result)