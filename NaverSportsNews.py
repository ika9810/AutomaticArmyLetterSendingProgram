import urllib.request
from bs4 import BeautifulSoup

def deleteSpan(details,length):
    listo = []
    a = '<span class=\"'
    b = '</span>'
    for i in range(1,length):
        c = details.split(a)[i].split(b)[0]
        article_split3 = a + c+ b
        listo.append(article_split3)
    return listo

BASEURL = "https://sports.news.naver.com"

response = urllib.request.urlopen(BASEURL).read()
soup = BeautifulSoup(response,"html.parser")
title = soup.find_all(class_="main_ranknews_list", id="mostViewedNewsList")
for j in range(1,3):
    splitURL = str(title).split("href=\"")[j].split("\" onclick=")[0].replace('amp;','')
    url = BASEURL + splitURL
    #print(url)
    mainResponse = urllib.request.urlopen(url).read()
    soup_article = BeautifulSoup(mainResponse,"html.parser")

    title_article = soup_article.find_all(class_="news_headline")
    detail_article = soup_article.find_all(id="newsEndContents")
    article_title = str(title_article).split("<h4 class=\"title\">")[1].split("</h4>")[0]

    article_split1 = str(detail_article).replace('<div class=\"news_end\" id=\"newsEndContents\">','') #원본
    length = len(article_split1.split(article_spliter1))
    test1 = deleteSpan(article_split1,length)
    for i in range(len(test1)):
        article_split1 = article_split1.replace(test1[i],'')
    final = article_split1.replace('<br/>','').split("<p class=\"")[0].replace('<div>','').replace('</div>','').split("<a href=\"")[0]
    #print(final)
    print(article_title + final)
#print(article_split4)
# main_ranknews_list
# mostViewedNewsList
