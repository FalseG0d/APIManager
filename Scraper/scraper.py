import requests as re
from bs4 import BeautifulSoup
from .models import Game,Article


def game_Scraper():
    url="https://falseg0d.itch.io/"

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    context=[]

    for link in soup.find_all('a',class_="title game_link"):
        context.append(link.string)

    for link in soup.find_all('a',class_="thumb_link game_link"):
        context.append(link.get('href'))

    for link in soup.find_all('div',class_="game_thumb"):
        context.append(link.get('style').split('\'')[1])

    for link in soup.find_all('div',class_="game_text"):
        context.append(link.string)

    for link in soup.find_all('div',class_="game_genre"):
        context.append(link.string)


    Game.objects.filter(scrapable=True).delete()
    x=len(context)/5
    x=int(x)

    for i in range(x):
        game=Game(name=context[i],itch_link=context[x*1+i],image=context[x*2+i],description=context[x*3+i],genre=context[x*4+i],scrapable=True)
        
        game.save()


def article_Scraper():
    url="https://gargapoorv1011.medium.com/"

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')
    context=[]

    soup=soup.find('div',class_='ai aj ak al am fc ao v')

    flags=soup.find_all('section',class_='db ga gb cw gc')

    for flag in flags:
        # print(flag)
        # print("\n\n\n")

        link=flag.find('a')
        
        link='https://gargapoorv1011.medium.com'+link.get('href')
        
        title=flag.find('a').string
        
        para=''

        for tag in flag.find_all('p'):
            para+=str(tag.string)
        
        article=Article(name=str(title),link=str(link),abstract=str(para),scrapable=True)
        # if article!=None:
        article.save()