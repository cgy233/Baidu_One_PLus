import json
import os
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw

def putChineseText(img, content):
	img = Image.fromarray(img)
	font_path = './msyh.ttf' # linux os font path:locate *.ttf copy path to this.
	font = ImageFont.truetype(font_path, 22) # 字体大小
	font_color = (255, 0, 0, 0) # b g r a
	draw = ImageDraw.Draw(img)
	draw.text((10, 10), content, font=font, fill=font_color)
	return np.array(img)

json_path = './data/British_Shorthair_141.json'	
save_path = './result/British_Shorthair_141_detected.jpg'

if not os.path.exists('./result'):
	os.mkdir('./result')

with open(json_path, 'rb') as jf:
	json_string = json.load(jf)
	for key in json_string['flags'].keys():
		if json_string['flags'][key]:
			img_path = json_string['imagePath']
			img = cv2.imread('./data/' + img_path)
			img = putChineseText(img, key)
			cv2.imwrite(save_path, img)