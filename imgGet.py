from selenium import webdriver
import time
import random, string
from urllib import request,parse
import urllib.request
from PIL import ImageGrab
import base64
import json
import requests
import re

def vercode():       
	# x = 1105 #1872,1052,
	# y = 405 #688,438
	# w = x + 190 #275,260
	# h = y + 40 #50,38
	# size = (x, y, w, h)
	# img = ImageGrab.grab(size)
	# img.save("C:/Users/moxi/Downloads/1.png")  # /Users/iwtay/Downloads/images/1.png
	# img.show()
	#
	# time.sleep(1)

	appkey = "62a8949082d27515eeafbd101b64912a"
	with open("D:/Downloads/1.png", 'rb') as f:
		base64_data = base64.b64encode(f.read())
		s = base64_data.decode()
		# print(s)

	textmob = {
		"key": appkey,
		"codeType": 4006,
		"base64Str": s
	}
	textmob = parse.urlencode(textmob).encode(encoding='utf-8')
	# print(textmob)

	req = urllib.request.Request(url="http://op.juhe.cn/vercode/index", data=textmob)
	webpage = urllib.request.urlopen(req)
	html = webpage.read()
	res = json.loads(html)
	yzm = str(res["result"])
	print(yzm)
vercode()