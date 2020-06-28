import requests
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd


def get_info(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    cookie = '__mta=140762765.1593345517354.1593354188089.1593354342319.6; uuid_n_v=v1; uuid=B3ACF2D0B93611EA8C8DE3118EB8AC1A1C0837E3568C489E8DF32213072595FA; _csrf=bf9956d6fd47ed87f19000c36a2d20856e3ccb44ee4c4742f520cc4a9a547902; _lxsdk_cuid=172facb2659c8-0f4ff6fb7839a5-e353165-1fa400-172facb2659c8; _lxsdk=B3ACF2D0B93611EA8C8DE3118EB8AC1A1C0837E3568C489E8DF32213072595FA; mojo-uuid=e2e993837c687a41fb16dc39f004d710; mojo-session-id={"id":"279cb871b311308963f88e7e79f04814","time":1593350761693}; lt=s27z8VIHz5dKEGJaGJuM8Dy4y9EAAAAA5woAAK4O34d1m-rZDJDWsFY4-08vqgRGG9BYam3bEuGhcnRYt8xldmH0fQN2SDc2MFclNg; lt.sig=6jwByTCvgsZv6VV1rRj_j6W4cXA; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593350834,1593350927,1593353199,1593354235; __mta=140762765.1593345517354.1593354188089.1593354235282.6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593354342; mojo-trace-id=17; _lxsdk_s=172fb4029b2-33c-25a-e5f%7C133424877%7C23'
    header = {'user-agent': user_agent, 'cookie': cookie}
    myurl = 'https://maoyan.com/films?showType=3'
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    movie = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-item film-channel"'}):
        for tag in tags.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
            for i in tag.find_all('span', attrs={'class': 'hover-tag'}):
                if i.text == '类型:':
                    movie_category = (i.find_parent('div').text.strip())  
                if i.text == '上映时间:':
                    movie_date = (i.find_parent('div').text.strip())
                    movie_title = i.find_parent('div').get('title')  
                    movie_info = [movie_title, movie_category, movie_date]
                    movie.append(movie_info)

    sleep(5)

    df = pd.DataFrame(movie[:10], columns=['movie-title', 'movie-category', 'movie-date'])
    df.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)

