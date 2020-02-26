# encoding: utf-8

from selenium import webdriver
import time
from PIL import ImageGrab
from chaojiying import Chaojiying_Client
import random
from urllib import request,parse
import urllib.request
import base64
import json
from config_data import deviceall
import requests
import re

class filter():
    sign_up = 'https://890cp2.com'

    def setUp(self):
        self.device = deviceall[5]  #deviceall[4]
        print(self.device)
        pixel_ratio = 3.0
        mobileEmulation = {"deviceMetrics": {"width": self.device['width'], "height": self.device['height'], "pixelRatio": pixel_ratio},"userAgent": self.device['ua']}
        options = webdriver.ChromeOptions()
        # options.binary_location = "C:/Users/moxi/Desktop/mychrome/Chrome/chrome.exe"
        # chrome_driver_binary = "chromedriver.exe"
        options.binary_location = "C:/Program Files (x86)/Google\Chrome/Application/chrome.exe"  # C:/Users/moxi/Desktop/mychrome/Chrome/chrome.exe
        chrome_driver_binary = "chromedriver76.exe"  # chromedriver.exe
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        # self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        self.driver = webdriver.Chrome(chrome_driver_binary, options=options)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(self.sign_up)
        self.driver.implicitly_wait(30)


    def quit(self):
        self.driver.quit()

    def verify(self):

        # self.driver.find_element_by_class_name("popupNotice_closeBtn___bVSp8").click()
        self.driver.find_element_by_xpath('//button[@class="popupNotice_closeBtn___bVSp8"]').click()
        for i in range(1,3) :
            self.driver.refresh()
            time.sleep(5)
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            # self.driver.find_element_by_class_name("barTextButton___G3WVC").click()
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@src,'/login')]"))

            username ="bq09221"
            pwd = "HWIsMRCrbl"
            print("User:"+username)
            print("Pwd:"+pwd)

            time.sleep(1)

            # user = self.driver.find_element_by_xpath('//input[@id="username"]')
            user = self.driver.find_element_by_id("username")
            user.clear()
            user.send_keys(username)
            # passw = self.driver.find_element_by_xpath('//input[@id="password"]')
            passw = self.driver.find_element_by_find_id("password")
            passw.send_keys(pwd)
            # code = self.driver.find_element_by_xpath('//input[@id="validateCode"]')
            code = self.driver.find_element_by_id("validateCode")
            code.send_keys("")

            time.sleep(1)

            x = self.device['xy']['x']  # 1872
            y = self.device['xy']['y']  # 688,438
            w = x + 205  # 275,230
            h = y + 40  # 50,38
            size = (x, y, w, h)
            img = ImageGrab.grab(size)
            img.save("C:/Users/moxi/Downloads/1.png")  # /Users/iwtay/Downloads/images/1.png
            # img.show()

            time.sleep(1)

            # chaojiying = Chaojiying_Client('iwtay77', 'Iwt.ay77','ac212bb67ed8fce6a530514d9f478093')  # 用户中心>>软件ID 生成一个替换 96001
            # im = open('/Users/iwtay/Downloads/images/1.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
            # yzm = chaojiying.PostPic(im, 1902)
            # print(yzm)
            # time.sleep(5)

            appkey = "62a8949082d27515eeafbd101b64912a"
            with open("C:/Users/moxi/Downloads/1.png", 'rb') as f:
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

            code.send_keys(yzm)
            time.sleep(1)
            self.driver.find_element_by_xpath('//button[@id="submit"]').click()
            print(i)
            if i == 1 :
                time.sleep(2)
                quit = self.driver.find_elements_by_xpath('//button[@class="quickAccessBarBtn___1F1-B"]')[7]
                quit.click()
                time.sleep(1)
                sure = self.driver.find_element_by_class_name("ant-btn.ant-btn-primary")
                if sure:
                    sure.click()
                    time.sleep(5)
            else:
                break

        time.sleep(2)

        sideNav_list = self.driver.find_elements_by_xpath('//button[@class="sideNav_anchor___1D7s9"]')
        sideNav =random.choice(sideNav_list)
        sideNav.click()

        rand = self.driver.find_elements_by_class_name("gameCal_ctrlBtn___38COx")[2]
        add = self.driver.find_elements_by_class_name("theme1___341L1.undefined button___3xxsI")[1]

        rand.click()
        add.click()

        rand.click()
        add.click()

        rand.click()
        add.click()

        rand.click()
        add.click()

        rand.click()
        add.click()

        self.driver.find_element_by_xpath('//button[@data-position="bottom"]').click()
        time.sleep(3)

        url = "http://200019.ip138.com/"
        req = urllib.request.urlopen(url).read()
        print(req)
        theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", str(req))
        ip = theIP[0]
        print("your IP Address is: ", ip)

        time.sleep(5)

        betss = self.driver.find_element_by_xpath('//div[@class="gameCart_response___T0czT"]').text
        if betss == "投注成功祝您中奖":
            print("投注成功祝您中奖!")
            response = requests.post(
                f"http://47.75.184.28/api/imessage-server/imessage-restapi/external/markEmail?email={username}&ip={ip}")
            print(response.status_code)

        time.sleep(3)



if __name__ == "__main__":
    F = filter()
    F.setUp()
    F.verify()
    F.quit()


