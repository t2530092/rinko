import numpy as np
import matplotlib.pylab as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#def step_function(x):
#    if x > 0:
#        return 1
#    else:
#        return 0

def step_function(x):
    y = x > 0
    return y.astype(np.int)

def indentify_function(x):
    return x

#X = np.array([1, 2])
#print(X.shape)

#W = np.array([
    #[1, 3, 5],
    #[2, 4, 6]])
#print(W)
#print(W.shape)

#Y = np.dot(X, W)
#print(Y)

X = np.array([1.0, 0.5])
W1 = np.array([
    [0.1, 0.3, 0.5],
    [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
print(W1.shape)
print(X.shape)
print(B1.shape)
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

W2 = np.array([
    [0.1, 0.4],
    [0.2, 0.5],
    [0.3, 0.6]])

B2 = np.array([0.1, 0.2])
print(Z1.shape)
print(W1.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([
    [0.1, 0.3],
    [0.2, 0.4]])

B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = indentify_function(A3)

for y in Y:
    print(y)
