# encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import ErrorInResponseException
import time
import random, string
from PIL import ImageGrab
import requests
import re
import base64
import urllib.request
from urllib import request,parse
import json
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

class filter():
    # sign_up = 'https://890cp2.com/register/?pt=808090'
    sign_up = 'https://890cp2.com/register/'  #  https://978cp8.com/register/?pt=978118
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

        ua_ph = random.choice(ua_iphone)
        ua_pa = random.choice(ua_ipad)

        xy5 = {'x': 235, 'y': 500}  # iphone5_se(235,510,205,40)
        xy678 = {'x': 317, 'y': 462}  # iphone6_7_8(320,475,205,40)
        xy678p = {'x': 375, 'y': 462}  # iphone6_7_8plus(375,470,205,40)
        xyx = {'x': 317, 'y': 462}  # iphoneX(320,475,205,40)
        xypad = {'x': 720, 'y': 462}  # ipad(720,475,205,40)
        xypadp = {'x': 915, 'y': 462}  # ipadpro(915,475,205,40)

        iphone5_se = {'width': 320, 'height': 568, 'ua': ua_ph, 'xy': xy5}
        iphone6_7_8 = {'width': 375, 'height': 667, 'ua': ua_ph, 'xy': xy678}
        iphone6_7_8plus = {'width': 414, 'height': 736, 'ua': ua_ph, 'xy': xy678p}
        iphoneX = {'width': 375, 'height': 812, 'ua': ua_ph, 'xy': xyx}
        ipad = {'width': 768, 'height': 1024, 'ua': ua_pa, 'xy': xypad}
        ipadPro = {'width': 1024, 'height': 1366, 'ua': ua_pa, 'xy': xypadp}

        deviceall = [iphone5_se, iphone6_7_8, iphone6_7_8plus, iphoneX, ipad, ipadPro]   #

        return deviceall

    def setUp(self):
        global driver
        count = 0
        while 1:
            try:
                count += 1
                print(count)
                r = requests.get(self.sign_up)
                print(r)
                if r:
                    try:
                        device_all = self.device_ua()
                        self.device = random.choice(device_all)
                        # self.device = device_all[5]
                        print(self.device)
                        pixel_ratio = 3.0
                        mobileEmulation = {"deviceMetrics": {"width": self.device['width'], "height": self.device['height'],
                                                             "pixelRatio": pixel_ratio}, "userAgent": self.device['ua']}
                        capa = DesiredCapabilities.CHROME
                        capa["pageLoadStrategy"] = "none"
                        options = webdriver.ChromeOptions()
                        options.binary_location = "C:/Program Files (x86)/Google\Chrome/Application/chrome.exe"  # C:/Users/moxi/Desktop/mychrome/Chrome/chrome.exe
                        chrome_driver_binary = "chromedriver76.exe"  # chromedriver.exe
                        options.add_experimental_option('mobileEmulation', mobileEmulation)
                        driver = webdriver.Chrome(chrome_driver_binary, options=options, desired_capabilities=capa)
                        wait = WebDriverWait(driver, 45)
                        driver.get(self.sign_up)
                        driver.maximize_window()
                        time.sleep(2)
                        driver.refresh()
                        # time.sleep(2)
                        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.form-inputImg')))
                        # time.sleep(1)
                        locator = (By.ID, "register-toggle")
                        text = "免费试玩"
                        # time.sleep(1)
                        wait.until(EC.text_to_be_present_in_element(locator, text))
                        time.sleep(1)
                        result = EC.text_to_be_present_in_element(locator, text)(driver)
                        print(result)
                        driver.execute_script("window.stop();")

                        # self.driver.set_page_load_timeout(30)
                        time.sleep(3)

                    except Exception as err:
                        print("未知错误 %s" % err)

                    break
                else:
                    print("Timeout")
                    driver.quit()
                    # continue
            except Exception as err:
                print("UnknownError %s" % err)
                driver.quit()
                # continue

    def quit(self):
        driver.quit()

    def random_user(self):
        # while 1:
        userl = ""
        userd = ""
        username = ""
        pwd = ""
        num = string.ascii_letters + string.digits
        lowercase = string.ascii_lowercase
        digits = string.digits
        num = string.ascii_letters + string.digits
        randl = random.randrange(3, 6)
        dd = 12 - randl
        randd = random.randrange(3, dd)
        for i in range(1,randl):
            userl += random.choice(lowercase)
        for i in range(1,randd):
            userd += random.choice(digits)
        username = userl + userd
        for i in range(6, 16):
            pwd += random.choice(num)

        return username, pwd
        # pattern = re.compile('[0-9]+')
        # match = pattern.findall(username)

        # if match:
        #     return username, pwd
        #
        #     break
        #
        # else:
        #     continue

    def validcode(self):
        x = self.device['xy']['x']  # 1872
        y = self.device['xy']['y']  # 688,438
        w = x + 205  # 275,230
        h = y + 40  # 50,38
        size = (x, y, w, h)
        img = ImageGrab.grab(size)
        img.save("D:/Downloads/1.png")  # /Users/iwtay/Downloads/images/1.png
        # img.show()

        time.sleep(1)
        #
        # chaojiying = Chaojiying_Client('iwtay77', 'Iwt.ay77', 'ac212bb67ed8fce6a530514d9f478093')  # 用户中心>>软件ID 生成一个替换 96001
        # im = open('C:/Users/moxi/Downloads/1.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        # yzm = chaojiying.PostPic(im, 4006)
        # print(yzm)
        # time.sleep(6)

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
        return yzm


    def verify(self):
        rand_user = self.random_user()
        username = rand_user[0]
        pwd = rand_user[1]
        print("User:"+rand_user[0])
        print("Pwd:"+rand_user[1])
        time.sleep(1)
        user = driver.find_element_by_id("username")
        user.send_keys(username)
        passw = driver.find_element_by_id("password")
        passw.send_keys(pwd)
        rpassw = driver.find_element_by_id("repeatPassword")
        rpassw.send_keys(pwd)
        code = driver.find_element_by_id("validateCode")
        code.send_keys("")
        # self.driver.find_element_by_id("submit").click()

        time.sleep(10)

        yzm = self.validcode()

        driver.find_element_by_id("validateCode").send_keys(yzm)
        time.sleep(3)
        driver.find_element_by_id("submit").click()
        # self.driver.find_element_by_id("submit").click()
        time.sleep(1)


        # info = self.driver.find_elements_by_tag_name("span")
        infos = driver.find_elements_by_xpath('//div[@id="success-msg"]')
        infoe = driver.find_elements_by_xpath('//div[@id="err-msg"]')
        # print(info)
        Mess0 = "注册成功!"
        MessA = "用户名校验失败，请输入4-11位字母和数字，至少含有一个字母"
        MessB = "密码校验失败，请输入大小写字母和数字组成的6-15个字符"
        MessC = "重复密码校验失败，请重复输入一样的密码"
        MessD = "验证码错误"
        MessE = "用户名由数字和字母组成,且长度在4-11位之间"
        MessF = "验证码是必填项不能为空"
        MessG = "验证码校验失败，请输入图片里的号码"
        for content in infoe:
            time.sleep(1)
            alertInfo = content.text
            print(alertInfo)
            if alertInfo == MessD or alertInfo == MessF or alertInfo == MessG:
                driver.find_element_by_id("validateCode").click()
                yzm = self.validcode()
                driver.find_element_by_id("validateCode").send_keys(yzm)
                time.sleep(3)
                driver.find_element_by_id("submit").click()
                time.sleep(3)
            else:
                # time.sleep(2)
                # self.driver.quit()
                # break
                pass
        for content in infos:
            time.sleep(1)
            alertInfo = content.text
            print(alertInfo)
            # smsg = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'success-msg'), u'注册成功！'))
            if alertInfo == Mess0 or alertInfo == "": # smsg == True: or alertInfo == ""
                print("用户名:" + str(username) + " 密码:" + str(pwd))
                response = requests.post(f"http://47.75.184.28/api/imessage-server/imessage-restapi/external/save?email={username}&password={pwd}")
                print(response.status_code)
            else:
                user.clear()
                passw.clear()
                rpassw.clear()
                code.clear()

        # deviceToken = self.driver.execute_script("return localStorage.getItem('appDeviceToken')")
        # print(deviceToken)
        time.sleep(2)
        # driver.quit()

if __name__  ==  "__main__":
    while 1:
        try:
            print("当前时间： ", time.strftime('%Y.%m.%d %H:%M:%S ', time.localtime(time.time())))
            F = filter()
            F.setUp()
            F.verify()
            time.sleep(8)
            F.quit()
            # time.sleep(30)
            # print("我要休息")
            time.sleep(random.randint(60, 600))
            # print("休息了一会")
        except TimeoutError:
            print("TimeoutError")
            time.sleep(10)
            F.quit()
            continue
        except Exception as e:
            print("错误信息：%s" % e)
            time.sleep(10)
            F.quit()
            continue
