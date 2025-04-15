bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])

message = f"my first bicycle was a {bicycles[0].title()}"
print(message)

#p3.1
game_list = ["吹雪","白雪","初雪","深雪","叢雲","薄雲","磯波","白雲"]
for game_titie in game_list:
    print(game_titie)

#p3.2
for game_titie in game_list:
    print(f"hello {game_titie}")

#p3.3
for game_titie in game_list:
    print(f"I would like to play {game_titie}")

game_list[0] = "吹雪"
print(game_list)

game_list.append("武蔵")
print(game_list)

game_list1 = []
game_list1.append("大和")
game_list1.append("赤城")
game_list1.append("由良")
print(game_list1)

game_list1.insert(0, "妙高")
print(game_list1)

del game_list1[0]
print(game_list1)

popped_game = game_list1.pop()
print(popped_game)
print(game_list1)
print(f"The last game I owned was a {popped_game}")

dd_list = ["吹雪","白雪","初雪","深雪","叢雲","薄雲","磯波","白雲"]
dd_list.pop(1)
print(dd_list)
dd_list.remove("白雲")
print(dd_list)

#p3.4
dd_list = ["吹雪","白雪","初雪","深雪","叢雲","薄雲","磯波","白雲"]
for dd in dd_list:
    print(f"{dd} in list")

#p3.5
change_dd = "白雪"
count = 0
index = 0
for dd in dd_list:
    count = count + 1
    if dd == change_dd:
        dd_list[count - 1] = "秋月"
print(dd_list)

#p3.5
#del_list = {"深雪","磯波","初雪"}
#for del_dd in del_list:
#    dd_list.remove(del_dd)
#print(dd_list)

#p3.6
dd_list.insert(0, "綾波")
dd_list.insert(1, "朧")
dd_list.append("漣")
print(dd_list)

while len(dd_list) != 2 :
    dd_list.pop()

print(dd_list)

while len(dd_list) != 0 :
    dd_list.pop()

print(dd_list)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_number = list(range(2, 11, 2))
print(even_number)

