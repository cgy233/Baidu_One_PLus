# coding: utf-8
import cv2
import os
import random
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv

#给图片增加高斯噪声，计算花费很长时间
def gaussian_noise(src):
	image = src
	h, w, c = image.shape
	for row in range(h):
		for col in range(w):
			#获取三个高斯随机数
			#第一个参数：概率分布的均值，对应着整个分布的中心
			#第二个参数：概率分布的标准差，对应于分布的宽度
			#第三个参数：生成高斯随机数数量
			s = np.random.normal(0, 20, 3)
			#获取每个像素点的bgr值
			b = image[row, col, 0]  #blue
			g = image[row, col, 1]  #green
			r = image[row, col, 2]  #red\
			#给每个像素值设置新的bgr值
			image[row, col, 0] = clamp(b + s[0])
			image[row, col, 1] = clamp(g + s[1])
			image[row, col, 2] = clamp(r + s[2])
	return image

img_dir = './data'
files=os.listdir(img_dir)

for file in files:
	img = cv2.imread(os.path.join(img_dir, file))
	if random.randint(0, 1):
		img = img[::-1, :] # 垂直翻转
	else:
		img = img[:, ::-1] # 水平翻转
	img = gaussian_noise(img)
	img = cv2.resize(img, (256, 256)) # 调整大小
	cv2.imwrite('./flipped_' + file, img)