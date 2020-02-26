# encoding: utf-8

from selenium import webdriver
import time
from PIL import ImageGrab
from chaojiying import Chaojiying_Client
import random
from config_data import deviceall
import requests
import re
import urllib.request
import base64
from urllib import request,parse
import json


class filter():
    sign_up = 'https://890cp2.com/'
    def device_ua(self):
        ua_iphone = []
        ua_ipad = []
        with open("ua_iphone.txt", 'r') as f:
            for line in f:
                # uaph = f.readline()
                line = line.strip().split('\n')
                # print(line)
                ua_iphone.append(line[0])
            # print(ua_iphone)

        with open("ua_ipad.txt", 'r') as a:
            for line in a:
                line = line.strip().split('\n')
                ua_ipad.append(line[0])
            # print(ua_all)

        ua_ph = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X; tr-TR) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.1.1 Mobile/14B100 Safari/537.36 Puffin/5.2.0IP'
        ua_pa = random.choice(ua_ipad)

        xypad = {'x': 720, 'y': 475}  # ipad(720,475,205,40)
        xypadp = {'x': 915, 'y': 475}  # ipadpro(915,475,205,40)
        xy678 = {'x': 315, 'y': 430}  # iphone6_7_8(320,475,205,40)
        xyx = {'x': 320, 'y': 430}  # iphoneX(320,475,205,40)
        xy5 = {'x': 252, 'y': 430}  # iphone5_se(235,510,205,40)
        xy678p = {'x': 375, 'y': 430}  # iphone6_7_8plus(375,470,205,40)

        iphone5_se = {'width': 320, 'height': 568, 'ua': ua_ph, 'xy': xy5}
        iphone6_7_8 = {'width': 375, 'height': 667, 'ua': ua_ph, 'xy': xy678}
        iphone6_7_8plus = {'width': 414, 'height': 736, 'ua': ua_ph, 'xy': xy678p}
        iphoneX = {'width': 375, 'height': 812, 'ua': ua_ph, 'xy': xyx}
        ipad = {'width': 768, 'height': 1024, 'ua': ua_pa, 'xy': xypad}
        ipadPro = {'width': 1024, 'height': 1366, 'ua': ua_pa, 'xy': xypadp}

        deviceall = [iphone5_se, iphone6_7_8, iphone6_7_8plus, iphoneX, ipad,ipadPro]   #

        return deviceall

    def setUp(self):
        device_all = self.device_ua()
        # self.device = random.choice(device_all)
        self.device = device_all[2]
        print(self.device)
        pixel_ratio = 3.0
        mobileEmulation = {"deviceMetrics": {"width": self.device['width'], "height": self.device['height'], "pixelRatio": pixel_ratio},"userAgent": self.device['ua']}
        options = webdriver.ChromeOptions()
        options.binary_location = "C:/Users/moxi/Desktop/mychrome/Chrome/chrome.exe"
        chrome_driver_binary = "chromedriver.exe"
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
        for i in range(1, 3):
            time.sleep(2)
            self.driver.find_elements_by_class_name("am-modal-button")[0].click()
            # self.driver.find_element_by_xpath('//div[@class="am-modal-button-group-h.am-modal-button-group-normal"]/a').click()
            # self.driver.refresh()
            time.sleep(5)
            self.driver.find_elements_by_class_name("barTextButton___G3WVC")[1].click()
            # self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@src,'/login')]"))

            username ="ti626"
            pwd = "zspQjn0d5Z"
            print("User:"+username)
            print("Pwd:"+pwd)

            # user = self.driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]')
            user = self.driver.find_elements_by_xpath('//input[@type="text"]')[0]
            time.sleep(2)
            user.clear()
            time.sleep(2)
            user.send_keys(username)
            passw = self.driver.find_element_by_xpath('//input[@type="password"]')
            passw.send_keys(pwd)
            code = self.driver.find_elements_by_xpath('//input[@type="text"]')[1]
            code.send_keys("")

            time.sleep(1)

            x = self.device['xy']['x']  # 1872
            y = self.device['xy']['y']  # 688,438
            w = x + 205  # 275,230
            h = y + 40  # 50,38
            size = (x, y, w, h)
            img = ImageGrab.grab(size)
            img.save("C:/Users/moxi/Downloads/1.png")  #  C:/Users/moxi/Downloads/1.png
            # img.show()

            time.sleep(5)

            # chaojiying = Chaojiying_Client('iwtay77', 'Iwt.ay77','ac212bb67ed8fce6a530514d9f478093')  # 用户中心>>软件ID 生成一个替换 96001
            # im = open('C:/Users/moxi/Downloads/1.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
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
            time.sleep(2)
            self.driver.find_elements_by_xpath('//button[@class="color1___3wpTZ"]')[0].click()
            print(i)
            if i == 1 :
                time.sleep(2)
                quit = self.driver.find_elements_by_xpath('//div[@class="am-tab-bar-tab"]')[4]
                time.sleep(2)
                quit.click()
                time.sleep(1)
                self.driver.find_element_by_class_name("iconService___BeN5z").click()
                time.sleep(1)
                self.driver.find_element_by_class_name("color1___3wpTZ").click()
                time.sleep(1)
                self.driver.refresh()
            else:
                break

        time.sleep(2)
        url = "http://200019.ip138.com/"
        req = urllib.request.urlopen(url).read()
        # print(req)
        theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", str(req))
        ip = theIP[0]
        print("your IP Address is: ", ip)
        time.sleep(2)
        response = requests.post(
            f"http://47.75.184.28/api/imessage-server/imessage-restapi/external/markEmail?email={username}&ip={ip}")
        print(response.status_code)
        time.sleep(2)
        # deviceToken = self.driver.execute_script("return localStorage.getItem('appDeviceToken')")
        # print(deviceToken)

        sideNav_list = self.driver.find_elements_by_xpath('//div[@class="listItem___12frK"]')
        sideNav =random.choice(sideNav_list)
        time.sleep(2)
        sideNav.click()
        time.sleep(2)
        self.driver.find_elements_by_class_name("theme1___341L1.undefined.button___3xxsI")[0].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name("buttonItem___2sWKk")[2].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name("iconRemove___3CKmq")[0].click()
        time.sleep(7)
        # self.driver.find_element_by_xpath('//div[@class="theme1___341L1.undefined.button___3xxsI"]').click()
        # time.sleep(2)
        self.driver.find_element_by_class_name("theme1___341L1.undefined.button___3xxsI").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("color1___3wpTZ").click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@data-position="bottom"]').click()


if __name__ == "__main__":
    F = filter()
    F.setUp()
    F.verify()
    F.quit()


