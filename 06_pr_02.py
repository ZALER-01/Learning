# letter = """Dear {name},
# you are selected !
# Date = <|date|>"""

# name = input("Enter your name: ")
# date = input("Enter the date: ")
# letter = letter.replace("{name}", name)
# letter = letter.replace("<|date|>", date)
# print(letter)

#Write a program to detect double spaces in a string
# string_with_double_spaces = "This  is  a  string  with  double  spaces."
# string_with_double_spaces.find("  ")
# print("Double spaces found at index:", string_with_double_spaces.find("  "))

#write a program to find and replace double spaces with single space

# String_replace= " Hi Rituraj   how are you   doing today?  "
# String_replace.replace("  ", " ")
# print("String after replacing double spaces with single space:", String_replace.replace("  ", " "))

#write a program to format 

greeting_format = "Hi, {name} Good Morning"
name = input("Enter your name: ")
formatted_message = greeting_format.format(name=name)
print(formatted_message)
