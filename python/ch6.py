import random

print("====================print 6.1====================")
alien_0 = {"color":"green", "points":5}
print(alien_0["color"])
print(alien_0["points"])

#6.2.1 访问字典中的值
print("====================print 6.2.1==================")
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#6.2.2 添加键值对
print("====================print 6.2.2==================")
alien_0 = {"color":"green", "points":5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

#6.2.3 从创建一个空字典开始
print("====================print 6.2.3==================")
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

#6.2.4 修改字典中的值
alien_0 = {"color":"green"}
print(f"The alien is {alien_0["color"]}")

alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}")

alien_0 = {
            "x_position":0,
            "y_position":25,
            "speed":"medium"
            }

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New pposition: ({alien_0["x_position"]}, {alien_0["y_position"]})")

#6.2.5 删除键值对
print("====================print 6.2.5==================")
alien_0 = {
    "color":"green",
    "points":5 
    }
del alien_0["points"]
print(alien_0)

#6.2.6 由类似的对象组成的字典
print("====================print 6.2.6==================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages["sarah"].title()
print(f"Sarah`s favorite language is {language}.")

#6.2.7 使用 get() 来访问值
print("====================print 6.2.7==================")
alien_0 = {'color': 'green', 'speed': 'slow'}
#error KeyError: 'points'
#print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#p6.1 练习 6.1：人
print("====================print p6.1==================")
persion = {
    "first_name":"xxx",
    "last_name":"yyy",
    "age":12,
    "city":"zzz"
}

for value in persion.values():
    print(value)

#p6.2 练习 6.2：喜欢的数 1
print("====================print p6.2==================")
favorite_numbers = {
    "Aria":42,
    "Jaxon":87,
    "Liora":16,
    "Zane":73,
    "Elira":29
}

for name in favorite_numbers.keys():
    print(f"{name}`s favorite number is {favorite_numbers[name]}.")


#p6.3 练习 6.3：词汇表 1 
print("====================print p6.3==================")

python_keywords = {
    "def":"Used to define a function",
    "if":"Starts a conditional statement.",
    "for":"Starts a loop that iterates over a sequence (like a list or string).",
    "return":"Exits a function and optionally returns a value.",
    "import":"Used to include external modules or libraries in your code."
}

for keywords in python_keywords:
    print(f"{keywords} : \n {python_keywords[keywords]}")

#6.3 遍历字典
#6.3.1 遍历所有的键值对
print("====================print 6.3.1==================")
user_0 = {
    "username": "efermi",
    "first": "enrice",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


#6.3.2 遍历字典中的所有键
print("====================print 6.3.2====================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


#6.3.3 按特定的顺序遍历字典中的所有键
print("====================print 6.3.3====================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#6.3.4 遍历字典中的所有值
print("====================print 6.3.4====================")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("====================================================")
for _,language in favorite_languages.items():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#p6.4 词汇表 2 
print("====================print p6.4====================")
python_keywords = {
    "def":"Used to define a function",
    "if":"Starts a conditional statement.",
    "for":"Starts a loop that iterates over a sequence (like a list or string).",
    "return":"Exits a function and optionally returns a value.",
    "import":"Used to include external modules or libraries in your code."
}

for key,value in python_keywords.items():
    print(f"{key}:\n \t{value}")

#append five keywords
print("====================================================")
python_keywords["class"] = "Used to define a new user-defined class (object-oriented programming)."
python_keywords["while"] = " Starts a loop that runs as long as a condition is True."
python_keywords["try"] = "Used to write exception-handling code that lets you catch and manage errors."
python_keywords["in"] = "Checks whether a value exists within a sequence (like a list, string, or tuple)."
python_keywords["None"] = "Represents the absence of a value or a null value."

for key,value in python_keywords.items():
    print(f"{key}:\n \t{value}")

#p6.5 河流 
print("====================print p6.5====================")
rivers = {
    "Nile":"Egypt",
    "Amazon":"Brazil",
    "Danube":"Germany",
    "Yangtze":"China",
    "Mississippi":"United States",
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

#p6.6 调查
print("====================print p6.6====================")
favorite_languages = {
    'Jen': 'python',
    'Sarah': 'c',
    'Edward': 'rust',
    'Phil': 'python',
}

name_list = [
    "Jen",
    "Sarah",
    "Edward",
    "Phil",
    "Emily",
    "Lucas",
    "Olivia",
    "Nathan",
    "Zoe",
    "Michael",
]

for name in name_list:
    if name in favorite_languages.keys():
        print(f"thank you {name}")
    else:
        print(f"{name} :(")

#6.4 嵌套
#6.4.1 字典列表
print("====================print 6.4.1====================")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
#创建30个外星人 
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens:{len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == "green":
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

#6.4.2 在字典中存储列表
#存储顾客所点比萨的信息
print("====================print 6.4.2====================")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#概述顾客点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}`s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#6.4.3 在字典中存储字典
users = {
    "aeinstein": {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\n Username: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#p6.7 练习 人们 
print("====================print p6.7==================")

people1 = {
    "first_name":"Emily",
    "last_name":"Carter",
    "age":29,
    "city":"Seattle"
}

people2 = {
    "first_name":"Daniel",
    "last_name":"Kim",
    "age":35,
    "city":"New York"
}

people3 = {
    "first_name":"Aisha",
    "last_name":"Hassan",
    "age":42,
    "city":"London"
}

peoples = [people1, people2, people3]

random.shuffle(peoples)
for people in peoples:
    print(f"user name : {people["first_name"]} {people["last_name"]}")
    print(f"age : {people["age"]}")
    print(f"city : {people["city"]}")

#p6.8 练习 宠物 
print("====================print p6.8==================")
pets = [
    {
        "pet_type":"Dog",
        "Pet_owner":"Emily Carter",
    },
    {
        "pet_type":"Cat",
        "Pet_owner":"Daniel Kim",
    },
    {
        "pet_type":"Parrot",
        "Pet_owner":"Aisha Hassan",
    },
    {
        "pet_type":"Rabbit",
        "Pet_owner":"Lucas Brown",
    },
    {
        "pet_type":"Hamster",
        "Pet_owner":"Sofia Martinez",
    },
]

random.shuffle(pets)
for pet in pets:
    print(f"pet type : {pet["pet_type"]}")
    print(f"pet owner : {pet["Pet_owner"]}\n")

#p6.9 喜欢的地方
print("====================print p6.9==================")
favorite_places = {
    "Emily Carter":"Kyoto, Japan",
    "Daniel Kim":"Grand Canyon, USA",
    "Aisha Hassan":"Santorini, Greece",
}

for name, place in favorite_places.items():
    print(f"{name}`s favorite place is {place}")