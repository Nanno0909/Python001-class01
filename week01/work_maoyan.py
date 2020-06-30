import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd


#定义函数，myurl为参数
def get_url_name(myurl):

    user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    cookie = '__mta=140762765.1593345517354.1593356898151.1593513839555.9; uuid_n_v=v1; uuid=B3ACF2D0B93611EA8C8DE3118EB8AC1A1C0837E3568C489E8DF32213072595FA; _lxsdk_cuid=172facb2659c8-0f4ff6fb7839a5-e353165-1fa400-172facb2659c8; _lxsdk=B3ACF2D0B93611EA8C8DE3118EB8AC1A1C0837E3568C489E8DF32213072595FA; mojo-uuid=e2e993837c687a41fb16dc39f004d710; _csrf=92ee8112f881f2c32ca2c0cb3925cb0927698a2b2476bda97ec183718ff90f96; mojo-session-id={"id":"0559d33bdc666732647dc4c9c4edea20","time":1593513633013}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593354235,1593354521,1593442774,1593513633; __mta=140762765.1593345517354.1593356898151.1593513633226.9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593513839; mojo-trace-id=2; _lxsdk_s=17304d065bd-418-ee1-b8d%7C%7C5'
    header = {'user-agent': user_agent, 'cookie':cookie}

    response = requests.get(myurl, headers=header)

    #用html的方式解析返回的网页内容
    bs_info = bs(response.text, 'html.parser')


    for i in bs_info.find_all('div', attrs={'class': 'movie-item film-channel'}, limit=10):
        film_url = []
        for i1 in i.find_all('a'):
            film_url.append(i.find_all('href'))
            #获取所有链接
            return(film_url)
            
            for i2 in file_url.find_all('div',attrs={'class': 'movie-brief-container'}):
                film_name = i2.find('h1','class').text
                film_ca =i2.find('li', 'class').text
                film_date = i2.find('li', 'class').text
            

            movie_list=[film_name, film_ca, film_date]

            film_list = pd.DataFrame(data = movie_list)

            film_list.to_csv('./film_list.csv', encoding='utf-8', index=False, header=False)

            


