import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

plt.rcParams['font.sans-serif'] = "SimHei" #设置字体为默认字体
mnist = tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y) = mnist.load_data()
plt.figure(figsize=(4,4))
for i in range(16):
    num = np.random.randint(1,10000)
    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.imshow(test_x[num],cmap="gray")
    plt.title("标签值:"+str(test_y[num]))


plt.tight_layout(rect=[0,0,1,0.9])
#设置图片标题
plt.suptitle("MNIST测试集样本",fontsize=20,color="red")
plt.show()