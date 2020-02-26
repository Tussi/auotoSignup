import sys
import random

ua_iphone = []
ua_ipad =[]
with open("ua_iphone.txt",'r') as f :
    for line in f:
        # uaph = f.readline()
        line = line.strip().split('\n')
        # print(line)
        ua_iphone.append(line[0])
    # print(ua_iphone)

with open("ua_ipad.txt",'r') as a :
    for line in a:
        line = line.strip().split('\n')
        ua_ipad.append(line[0])
    # print(ua_all)

ua_ph = random.choice(ua_iphone)
# ua_pa = random.choice(ua_ipad)
ua_pa = 'Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1'

# iphone5_se_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
# ipad_UA = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
# ipadPro_UA = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
# iphone6_7_8_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# iphone6_7_8plus_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# iphoneX_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1'
#

#web:
# xypad = {'x': 720, 'y': 475}  # ipad(720,475,205,40)
# xypadp = {'x': 915, 'y': 475}  # ipadpro(915,475,205,40)
# xy678 = {'x': 320, 'y': 475}  # iphone6_7_8(320,475,205,40)
# xyx = {'x': 320, 'y': 475}  # iphoneX(320,475,205,40)
# xy5 = {'x': 235, 'y': 510}  # iphone5_se(235,510,205,40)
# xy678p = {'x': 375, 'y': 470}  # iphone6_7_8plus(375,470,205,40)

#phones:
xypad = {'x': 720, 'y': 475}  # ipad(720,475,205,40)
xypadp = {'x': 915, 'y': 475}  # ipadpro(915,475,205,40)
xy678 = {'x': 315, 'y': 430}  # iphone6_7_8(320,475,205,40)
xyx = {'x': 320, 'y': 430}  # iphoneX(320,475,205,40)
xy5 = {'x': 252, 'y': 430}  # iphone5_se(235,510,205,40)
xy678p = {'x': 375, 'y': 430}  # iphone6_7_8plus(375,470,205,40)


iphone5_se = {'width': 320, 'height': 668, 'ua': ua_ph, 'xy': xy5}
iphone6_7_8 = {'width': 375, 'height': 667, 'ua': ua_ph, 'xy': xy678}
iphone6_7_8plus = {'width': 414, 'height': 736, 'ua': ua_ph, 'xy': xy678p}
iphoneX = {'width': 375, 'height': 812, 'ua': ua_ph, 'xy': xyx}
ipad = {'width': 768, 'height': 1024, 'ua': ua_pa, 'xy': xypad}
ipadPro = {'width': 1024, 'height': 1366, 'ua': ua_pa, 'xy': xypadp}

deviceall = [iphone5_se, iphone6_7_8, iphone6_7_8plus, iphoneX, ipad, ipadPro]