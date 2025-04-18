#p4-2
list_a = ["cat", "dog", "ant", "fish", "bird"]
for a in list_a:
    print(f"A {a} would make a great pet.")
print("Any of these animals would make a great pet!")

#4.3.1 使⽤ range() 函数
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

#4.3.2 使⽤ range() 创建数值列表
numbers = list(range(1, 6))
print(numbers)

even_number = list(range(2, 11, 2))
print(even_number)

square = []
for value in range(1, 11):
    value = value ** 2
    square.append(value)
print(square)

#4.3.3 对数值列表执⾏简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#4.3.4 列表推导式
square = [value ** 2 for value in range(1, 11)]
print(square)

#p4.3
for index in range(1, 21):
    print(index)

#p4.4
number_lsit = range(1, 1_000_001)
#for number in number_lsit:
#    print(number)
#p4.5

print(min(number_lsit))
print(max(number_lsit))
print(sum(number_lsit))

#p4.6 
p4_6list = list(range(1, 20, 2))
print(p4_6list)

#p4.7
p4_7list = [val * 3 for val in range(1, 11)]
print(p4_7list)
for p4_7 in p4_7list:
    print(p4_7)

#p4.8
p4_8_number_list = list(range(1, 11))
p4_8_list = []
for index in p4_8_number_list:
    p4_8_list.append(index ** 3)
for p4_8 in p4_8_list:
    print(p4_8)

#p4.9
p4_9list = [val ** 3 for val in range(1, 11)]
print(p4_9list)
for p4_9 in p4_9list:
    print(p4_9)

#4.4 使⽤列表的⼀部分
#4.4.1 切⽚
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#4.4.2 遍历切⽚
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']

# 这是⾏不通的：
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#p4.10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"The first three items in the list are:{players[:3]}")
print(f"Three items from the middle of the list are:{players[1:4]}")
print(f"The last three items in the list are:{players[-3:]}")

#p4.11
my_pizzas = ["Margherita", "Pepperoni", "Mushroom", "Prosciutto", "Bianca"]
friend_pizzas = my_pizzas[:]
friend_pizzas.append("Pepperoni")
print(f"My favorite pizzas are:{my_pizzas}")
print(f"My friend's favorite pizzas are:{friend_pizzas}")

#p4.12
for my in my_pizzas:
    print(my)

for friend in friend_pizzas:
    print(friend)

#4.5 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions = (200, 50)
#dimensions[0] = 250

#4.5.2
for dimension in dimensions:
    print(dimension)

#4.5.3 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#p4.13
food_group = ("Pizza", "Sushi", "Tacos", "Spaghetti", "Curry")
for food in food_group:
    print(food)

#food_group[0] = "Ramen"
food_group = ("Biryani", "Falafel", "Tacos", "Spaghetti", "Curry")
for food in food_group:
    print(food)