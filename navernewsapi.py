import requests
import pandas as pd
import pyperclip
import re

client_id = "" #1.에서 취득한 아이디 넣기
client_secret = ""  #1. 에서 취득한 키 넣기
searchlist = ['맥미니','lck',]
search_word = '맥미니' #검색어
encode_type = 'json' #출력 방식 json 또는 xml
max_display = 10 #출력 뉴스 수
sort = 'date' #결과값의 정렬기준 시간순 date, 관련도 순 sim
start = 1 # 출력 위치

url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

#헤더에 아이디와 키 정보 넣기
headers = {'X-Naver-Client-Id' : client_id,
           'X-Naver-Client-Secret':client_secret
           }

#HTTP요청 보내기
r = requests.get(url, headers=headers)
#요청 결과 보기 200 이면 정상적으로 요청 완료
c = r.json()['items']
result = ""
for i in range(len(c)):
    text =  c[i]['title']+'\n' + c[i]['description']+'\n\n'
    result += re.sub('<.+?>', '', text, 0, re.I|re.S)
#pd.DataFrame(r.json()['items'])
print(result)
pyperclip.copy(result) #클립보드에 복사
print('finish,', len(result))
