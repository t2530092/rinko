import matplotlib.pylab as plt
import math
import random
x = list(range(1,11,1))
y = x[:]

#x = random.shuffle(x)
#y = list(range(1,11,1))
count = 0
while count < 3:
    random.shuffle(y)
    plt.plot(x, y, label = f"count = :{count}")
    count = count + 1

plt.xlabel = ("x")
plt.ylabel = ("y")
plt.legend(loc=2)
plt.show()
