#4.2    损失函数
#4.2.1  均方误差    （平均二乗誤差） 
import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

# 平均二乗誤差  を　確認
#损失函数值越小，和监督数据之间的误差就越小
def test_mean_squared_error():
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    val = mean_squared_error(np.array(t), np.array(y))
    print(val)

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    val = mean_squared_error(np.array(t), np.array(y))
    print(val)

#交叉熵误差 交差エントロピー誤差 cross entropy error
def cross_entoropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

def test_cross_entoropy_error():
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    val = cross_entoropy_error(t, y)
    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    val = cross_entoropy_error(t, y)

def main():
    test_mean_squared_error()


#交叉熵误差

if __name__ == "__main__":
    main()

