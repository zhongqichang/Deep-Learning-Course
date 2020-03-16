import numpy as np
x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
#x2 = np.array([2,3,4,2,3,4,2,4,1,3])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

x1 = np.mean(x)#求均值
y1 = np.mean(y)

sum1 = np.sum((x-x1)*(y-y1))#求和
sum2 = np.sum(pow((x-x1),2))

w = sum1/sum2
b = y1-w*x1
print("w的值是:",w)
print("b的值是:",b)