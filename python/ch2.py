message = "Hello Python"
print(message)

message = "Hello Python Crash Course world!"
print(message)

message_1 = "This is a string"
message_2 = 'This is also a string'

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("python")
print("\t python")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = "python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

simple_url = "https://www.uec.ac.jp"
url = simple_url.removeprefix("https://")
print(url)

message = "One of Python's strengths is its diverse community."
#message = 'One of Python's strengths is its diverse community.'
print(message)

#p2.3
hello_message = "Hello"
text_message = "input message at here"
user_name = "yua"
print(f"{hello_message}! {user_name}, {text_message}")

#p2.4
text_name = "Ada name"
upper_text_name = text_name.upper()
lower_text_name = text_name.lower()
title_text_name = text_name.title()
print(upper_text_name)
print(lower_text_name)
print(title_text_name)

#p2.5
albert_message = '''Albert Einstein once said, "A person who never made a mistake never
tried anything new."'''
print(albert_message)

#p2.6
famous_person = "Albert Einstein"
albert_message = f'''{famous_person} once said, "A person who never made a mistake never
tried anything new."'''
print(albert_message)

#p2.7
person_name = '\tname\n'
person_name = person_name.rstrip()
person_name = person_name.lstrip()
person_name = person_name.strip()
print(person_name)

#p2.8
file_name = 'python_notes.txt'
file_name = file_name.removesuffix(".txt")
print(f"p2.8 output: {file_name}")

#p2.9
print(3 + 5)
print(9 - 1)
print(2 * 4)
print(int(24 / 3))