import math
print("请输入a,b,c的值")
a = int(input("请输入a,a不能等于0:"))
b = int(input())
c = int(input())
d = pow(b,2)-4*a*c #求德尔塔
# print(d)
if(d > 0):
    e = (-1*b+math.sqrt(d))/(2*a)
    f = (-1*b-math.sqrt(d))/(2*a)
    print("有两个解:%f,%f"%(e,f))
if(d == 0 ):
    e = -1*b/(2*a)
    print("有一个解:%f"%(e))
if(d < 0):
    print("无解")
