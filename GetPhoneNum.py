# -*- encoding=utf8 -*-
__author__ = "moxi"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import requests
import bs4
from bs4 import BeautifulSoup
import re
import random
import os


class PhoneCode():
    def getPho(self):
        page = ["1", "2", "3"]
        phlists = []
        for i in range(len(page)):
            p = page[i]
            #         p = 5
            url = f'https://www.yinsixiaohao.com/dl/{p}/.html'
            response = requests.get(url).text
            soup = bs4.BeautifulSoup(response, 'html.parser')
            result = soup.findAll(name='p', attrs={'class': 'layuiadmin-big-font card-phone'})
            phlist = []
            for j in result:
                ph = j.get("id")
                phlist.append(ph)
            phlists.extend(phlist)
        # print(phlists)
        self.pho = random.choice(phlists)
        # print(self.pho)
        return self.pho

    def getCode(self):
        ph = self.pho
        print(ph)
        ul = f"https://www.yinsixiaohao.com/message/{ph}.html"
        # ul = "https://www.yinsixiaohao.com/message/17134025281.html"
        #     content = urllib.request.urlopen(ul).read()
        #     phoneNum = re.findall(r'<td>(.*?)</td>',str(content))
        res = requests.get(ul)
        res.encoding = 'utf8'
        so = BeautifulSoup(res.text, 'html.parser')

        content = re.findall(r'<td>(.*?)</td>', str(so))
        #     print(ph)
        rry = r"人人盈"
        for cont in content:
            rr = re.search(rry, cont)
            if rr != None:
                co = int(cont[15:21])
                return co
            else:
                return "123456"

    def main(self):
    #     os.system('adb install C:\\Users\\moxi\Downloads\\com.gamerry.gamerry-v2.0.0.apk')
        #     sleep(10)
    #     touch(Template(r"tpl1568277064246.png", record_pos=(0.001, -0.007), resolution=(1600, 900)))
    #     # poco("人人盈棋牌").click()
    #     # assert_exists(Template(r"tpl1568616987322.png", record_pos=(0.412, -0.182), resolution=(1600, 900)), "请填写测试点")
    #     sleep(60)
    #     touch(Template(r"tpl1568598256359.png", record_pos=(0.411, -0.182), resolution=(1600, 900)))
    #
    #     touch(Template(r"tpl1568598303011.png", record_pos=(0.053, 0.111), resolution=(1600, 900)))
    #     touch(Template(r"tpl1568598349345.png", record_pos=(0.048, -0.069), resolution=(1600, 900)))
        pho = self.getPho()
        print(pho)
        sleep(20)
    #     text(pho)
    #     sleep(5)
    #     # touch(Template(r"tpl1568617793723.png", record_pos=(0.435, 0.218), resolution=(1600, 900)))
    #     poco("android.widget.Button").click()
    #
    #     touch(Template(r"tpl1568598383510.png", record_pos=(-0.006, 0.078), resolution=(1600, 900)))
    #     sleep(45)
        code = self.getCode()
        print("Code is : %s" % code)
    #     sleep(3)
    #     touch(Template(r"tpl1568598429042.png", record_pos=(0.04, 0.016), resolution=(1600, 900)))
    #     text(code)
    #     # touch(Template(r"tpl1568617793723.png", record_pos=(0.435, 0.218), resolution=(1600, 900)))
    #     poco("android.widget.Button").click()
    #     touch(Template(r"tpl1568598456320.png", record_pos=(0.003, 0.146), resolution=(1600, 900)))
    #     sleep(1.0)
    #     touch(Template(r"tpl1568598571775.png", record_pos=(-0.17, -0.06), resolution=(1600, 900)))
    #     while 1:
    #         touch(Template(r"tpl1568598588882.png", record_pos=(0.003, 0.235), resolution=(1600, 900)))
    #         sleep(10.0)
    #         touch(Template(r"tpl1568598619488.png", record_pos=(0.367, -0.234), resolution=(1600, 900)))
    #         #     touch(Template(r"tpl1568598652753.png", record_pos=(-0.451, -0.234), resolution=(1600, 900)))
    #         sleep(75.0)
    #         touch(Template(r"tpl1568598997125.png", record_pos=(-0.001, 0.15), resolution=(1600, 900)))
        #     touch(Template(r"tpl1568599081891.png", record_pos=(-0.141, 0.216), resolution=(1600, 900)))


if __name__ == '__main__':
    P = PhoneCode()
    P.main()




