import requests
from bs4 import BeautifulSoup

#def body_parts ():
    #headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    #data = requests.get('https://exrx.net/Lists/Directory',headers=headers)
    #
    #soup = BeautifulSoup(data.text, 'html.parser')
    #
    #bd_prts = soup.select('div.col-sm-6>ul>li>a')
    #for bd in bd_prts:
    #    print("*"*60)
    #    print(bd.text)



#def ex_wrkots ():
    #headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    #data = requests.get('https://exrx.net/Lists/ExList/NeckWt',headers=headers)
    #
    #soup = BeautifulSoup(data.text, 'html.parser')
    #
    #
    #ex_wo = soup.select('div.col-sm-6 > ul > li')
    #for ex in ex_wo:
    #    print("*"*60)
    #    print(ex.text.strip())



#def init_db_job():
    #db.sbsparta.insert_one({tiasdlfkama})
    #db.sbsparta.insert_one({tiasdlfkama})
    #db.sbsparta.insert_one({tiasdlfkama})


def gg_api ():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://developers.google.com/android/reference/com/google/android/gms/fitness/data/WorkoutExercises',headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    print(soup)
    #bd_prts = soup.select('div.col-sm-6>ul>li>a')
    #for bd in bd_prts:
        #print("*"*60)
        #print(bd.text)

gg_api()