import requests as re
from bs4 import BeautifulSoup


# def game_Scraper():
#     url="https://falseg0d.itch.io/"

#     r=re.get(url)
#     htmlcontent=r.content

#     soup=BeautifulSoup(htmlcontent,'html.parser')

#     context=[]

#     for link in soup.find_all('a',class_="title game_link"):
#         context.append(link.string)

#     for link in soup.find_all('a',class_="thumb_link game_link"):
#         context.append(link.get('href'))

#     for link in soup.find_all('div',class_="game_thumb"):
#         context.append(link.get('style').split('\'')[1])

#     for link in soup.find_all('div',class_="game_text"):
#         context.append(link.string)

#     for link in soup.find_all('div',class_="game_genre"):
#         context.append(link.string)


#     Game.objects.filter(scrapable=True).delete()
#     x=len(context)/5
#     x=int(x)

#     for i in range(x):
#         game=Game(name=context[i],itch_link=context[x*1+i],image=context[x*2+i],description=context[x*3+i],genre=context[x*4+i],scrapable=True)
        
#         game.save()

# color = {
#     '#563d7c': 'CSS',
#     '#3572A5': 'Python',
#     '#e34c26': 'HTML',
#     '#3178c6': 'TypeScript',
#     '#f34b7d': 'C++',
#     ''
# }

def medium_Scraper(url):

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    articles=soup.find_all('article')

    res = {}

    for article in articles:
        print(article)
        # print("\n\n\n")

        link=article.find('a')
        
        link ='https://gargapoorv1011.medium.com'+link.get('href').split('?')[0]
        
        date = article.find('a').string
        title = article.find('h2').string

        para=''

        for tag in article.find_all('p'):
            para+=str(tag.string)
        
        res[title] = {
            'title': str(title),
            'date': str(date),
            'link': str(link),
            'abstract': str(para),
        }

    return res


def github_Scraper(url):

    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    navBar=soup.find('nav', class_="UnderlineNav-body width-full p-responsive js-sidenav-container-pjax").find_all('a')

    res = {}

    res = {
        'repositories': navBar[1].find('span').contents[0],
        'project': navBar[2].find('span').contents[0],
        'packages': navBar[3].find('span').contents[0],
        'stars': navBar[4].find('span').contents[0]
    }

    # fameRepo=soup.find('ol').find_all('li')

    # print(famRepo)

    # for repo in fameRepo:
        # name = repo.find('p', class_="pinned-item-desc").contents[0].strip()
        # desc = repo.find('p', class_="pinned-item-desc").contents[0].strip()
        # name = repo.find('span', class_="repo").contents[0]
        # lang = repo.find('span', class_="repo-language-color")

        # if lang:
        #     print(color[lang.get('style').split(':')[1].strip()])

    # res['famousRepo'] = [famRepo]

    # for repo in famRepo:
    #     name = repo.find('span', class_="Label Label--secondary v-align-middle ml-1")
    #     lang = repo.find('span', itemprop_="programmingLanguage")
    #     desc = repo.find('p', class_="pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3")

    #     res['famousRepo'].append({
    #         'name': name,
    #         'language': lang,
    #         'description': desc
    #     })

    return res


# article_Scraper()