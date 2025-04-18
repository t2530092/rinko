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
p4_8list = [val ** 3 for val in range(1, 11)]
print(p4_8list)
for p4_8 in p4_8list:
    print(p4_8)