import requests as re
from bs4 import BeautifulSoup

def medium_Scraper(url):

    r=re.get(url)
    htmlcontent=r.content

    soup = BeautifulSoup(htmlcontent,'html.parser')

    articles = soup.find_all('article')

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

    navBar = soup.find('nav', class_="UnderlineNav-body width-full p-responsive js-sidenav-container-pjax").find_all('a')

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

def itch_Scraper(url):
    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    # print(soup)

    res = {}
    links = soup.find('div', class_="user_links").findAll('a')

    res['links'] = []

    for link in links:
        res['links'].append(link.get('href'))

    res['game'] = []
    games = soup.find_all('div', class_="game_cell")

    for game in games:
        # title = game.find('div', class_="title")
        # res['game'][title] = {
        #     'link' : game.find('a').get('href'),
        #     'about' : game.find('div', class_="game_text")
        # }

        image = game.find('img').get('data-lazy_src')
        content = game.find('div', 'game_text').contents[0]
        link = game.find('div', 'game_cell_data').find('a').get('href')
        title = game.find('div', 'game_cell_data').find('a').contents[0]

        res['game'].append(
                {
                'title': title,
                'image': image,
                'link': link,
                'content': content
                })

        # print(image + link)

    return res