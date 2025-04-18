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
#5.2.4 数值⽐较
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")