from fake_useragent import UserAgent
import requests
import time
import json
from selenium import webdriver

ua =UserAgent(verify_ssl=False)

headers ={
    'User-agent' : ua.random,
    'Referer': 'https://shimo.im/login?from=home'
}


with open('C:\\Users\\keith\\Desktop\\user.json') as user_file:
    josn_data = json.load(user_file)
    mobile = josn_data['user']
    password = josn_data['passwd']
    #print(mobile)
    #print(josn_data)

s =requests.Session()
 # 会话对象：在同一个 Session 实例发出的所有请求之间保持 Cookie,
 # 期间使用  urllib3 的 connection pooling 功能，
 # 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。

login_url = 'https://shimo.im/lizard-api/auth/password/login'

response = s.post(login_url, data=josn_data, headers=headers)
print(response.status_code)


    





""" 
try: 
    browser = webdriver.Chrome()
    #需要安装chrome driver，和浏览器版本保持一致
    #http://chromedriver.storage.googleapis.com/index.html
    

    browser.get('https://shimo.im')
    time.sleep(1)


    browser.switch_to_frame

 """