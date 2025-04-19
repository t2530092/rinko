import random
#5.1
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#5.2 条件测试
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')

#5.2.3 检查是否不等

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#5.2.4 数值⽐较
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#5.2.4 检查多个条件
age_0 = 22
age_1 = 18

print((age_0 >= 21) and (age_1 >= 21))
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print((age_0 >= 21 ) or (age_1 >= 21))

#5.2.6 检查特定的值是否在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(("mushrooms" in requested_topping))
print(('pepperoni' in requested_toppings))

#5.2.7 检查特定的值是否不在列表中
banned_users = ['andrew', 'carolina', 'david']
user = "marie"
if user not in banned_users:
    print(f"{user.title()},you can post a respone if you wish.")

#5.2.8 布尔表达式
game_active = True
can_edit = False

#p5.1

#p5.2
string_1 = "string_1"
string_2 = "string_1"
string_3 = string_1
print(string_1 == string_2)
print(string_1 == string_3)

#5.3.1
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#5.3.2
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else

print("====================print 5.3.3====================")
age = 12
if age < 4:
    print("your admission cost in $0.")
elif age < 18:
    print("your admission cost in $25.")
else:
    print("your admission cost in $40.")

#5.3.4 使用多个 elif 代码块
print("====================print 5.3.4====================")
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"you admission is ${price}.")

#5.3.5省略 else 代码块
print("====================print 5.3.5====================")
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"you admission is ${price}.")

#5.3.6 测试多个条件
print("====================print 5.3.6====================")
requested_toppings = ['mushrooms', 'extra cheese']

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("")
print("Finished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#p5.3
print("====================print p5.3====================")
alien_color = "green"
alien_color = "yellow"
alien_color = "red"

if alien_color == "green":
    print("you got 5 score!!!")
elif alien_color == "yellow":
    print("you got 10 score!!!")
elif alien_color == "red":
    print("you got 15 score!!!")

#p5.4
print("====================print p5.4====================")
alien_color = "green"
alien_color = "yellow"
alien_color = "red"

if alien_color == "green":
    print("you got 5 score!!!")
else:
    print("you got 10 score!!!")

#p5.5
print("====================print p5.5====================")
alien_color = "red"
if alien_color == "green":
    print("you got 5 score!!!!")
elif alien_color == "yellow":
    print("you got 10 score!!!!")
else:
    print("you got 15 score!!!!")

#p5.6
print("====================print p5.6====================")
age = 12
if (age >= 2) and (age < 4):
    print("a baby")
elif (age >= 4) and (age < 13):
    print("a child")
elif (age >= 13) and (age < 18):
    print("a young")
elif (age >= 18) and (age < 65):
    print("a middle")
elif (age >= 65):
    print("a old")
    
#p5.7
print("====================print p5.7====================")
favorite_fruits = ["Apple", "Banana", "Mango"]
check_favorite_fruits = ["Apple", "Banana", "Mango", "Pineapple", "Strawberry"]

random.shuffle(check_favorite_fruits)
for check_favorite_fruit in check_favorite_fruits:
    if check_favorite_fruit in favorite_fruits:
        print(f"You really like {check_favorite_fruit}!")

#5.4.1 if文を使う、リストを処理する
print("====================print 5.4.1====================")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#5.4.2 リストが空ではないことを確認する
print("====================print 5.4.1====================")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#5.4.3 複数のリストを使う
print("====================print 5.4.1====================")
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#p5.8
print("====================print p5.8====================")
admin_name = "admin"
user_names = ["admin", "alice", "bob", "charlie", "diana"]
random.shuffle(user_names)
for user_name in user_names:
    if (user_name == admin_name):
        print(f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")

#p5.9
print("====================print p5.9====================")
user_names = []
if user_names:
    random.shuffle(user_names)
    for user_name in user_names:
        if (user_name == admin_name):
            print(f"Hello {user_name}, would you like to see a status report?")
        else:
            print(f"Hello {user_name}, thank you for logging in again.")
else:
    print("we need to find some users!")

#p5.10 ユーザーの名前を確認する
print("====================print p5.10====================")
current_users = ["Emma", "Liam", "Olivia", "Noah", "Ava"]
new_users = ["Olivia", "Noah", "Sophia", "Ethan", "Mia"]
little_new_users = []
for current_user in current_users:
    little_new_users.append(current_user.lower())

random.shuffle(new_users)
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"name {new_user} has been used!!!")
    else:
        print(f"name {new_user} can be use!!!")
#p5.11 序数
print("====================print p5.11====================")
number_list = list(range(1, 10))
random.shuffle(number_list)
for number in number_list:
    if number == 1:
        print("1st")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
