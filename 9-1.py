import tensorflow as tf
import numpy as np

x1 = np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y = np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x0 = np.ones(len(x1))

X = np.stack((x0,x1,x2),axis=1)
Y = np.array(y).reshape(-1,1)

Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt,X))
XtX_1_Xt = tf.matmul(XtX_1,Xt)
W = tf.matmul(XtX_1_Xt,Y)

print("请输入房屋面积（20-500,实数）和房间数（1-10,整数），预测房屋销售价格：")
while True:
    x1_test = float(input("房屋面积："))
    x2_test = int(input("房间数："))
    if(not(x1_test >= 20 and x1_test <= 500)):
        print("房屋面积范围出错，请重新输入")
        continue
    if(not(x2_test >=1 and x2_test<=10)):
        print("房间数范围出错，请重新输入")
        continue
    if(not(isinstance(x1_test,float))):
        print("房屋面积类型出错，请重新输入")
        continue
    if(not(isinstance(x2_test,int))):
        print("房间数类型出错，请重新输入")
        continue
    
    y_pred = W[1]*x1_test+W[2]*x2_test+W[0]
    y_np = np.round(y_pred.numpy()[0],2)
    # y_np = y_pred.numpy()[0]
    print("预测价格：",y_np,"万元")


