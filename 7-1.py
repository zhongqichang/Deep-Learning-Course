import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] = "SimHei" #设置字体为默认字体
img = Image.open("lena.tiff")
img = img.resize((250,250))
img_r,img_g,img_b = img.split()
plt.figure(figsize=(10,10))
#R-缩放
img_small = img_r.resize((50,50))
plt.subplot(2,2,1)
plt.axis("off")
plt.title("R-缩放",fontsize=14) #设置标题
plt.imshow(img_small,cmap="gray")
#G-镜像+旋转
plt.subplot(2,2,2)
img_flr = img_g.transpose(Image.FLIP_LEFT_RIGHT) #水平翻转
img_t = img_flr.transpose(Image.ROTATE_270) #逆时针选择270°
plt.title("G-镜像+旋转",fontsize=14) #设置标题
plt.imshow(img_t,cmap="gray")
#B-裁剪
plt.subplot(2,2,3)
plt.axis("off")
img_region = img_b.crop((0,0,150,150))
plt.title("B-裁剪",fontsize=14) #设置标题
plt.imshow(img_region,cmap="gray")
#RGB
plt.subplot(2,2,4)
plt.axis("off")
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.title("RGB",fontsize=14) #设置标题
plt.imshow(img_rgb)
img_rgb.save("test.png")
#设置图片标题
plt.suptitle("图像基本操作",fontsize=20,color="blue")
plt.show()

