import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_,_) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif'] = "SimHei" #设置字体为默认字体
plt.rcParams['axes.unicode_minus'] = False

titles = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B-1000','LSSTAT','MEDV']

plt.figure(figsize=(12,12))

#用户输入属性
for i in range(13):
    print(i+1,'--',titles[i])

print("请选择属性:")
index = int(input())
plt.subplot(1,1,1)
plt.scatter(train_x[:,i],train_y)
plt.xlabel(titles[i])
plt.ylabel("Price($1000's)")
plt.title(str(index)+"."+titles[index-1]+" - Price")
plt.show()

#各个属性与房价的关系
# for i in range(13):
#     plt.subplot(4,4,(i+1))
#     plt.scatter(train_x[:,i],train_y)
#     plt.xlabel(titles[i])
#     plt.ylabel("Price($1000's)")
#     plt.title(str(i+1)+"."+titles[i]+" - Price")

# plt.tight_layout
# plt.suptitle("各个属性与房价的关系",x=0.5,y=1.0,fontsize=20)
# plt.show()




