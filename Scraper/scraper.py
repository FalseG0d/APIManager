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
        
        # This has to change and made Dynamic 
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

    res['famousRepo'] = []

    fameRepos=soup.find_all('li', class_="mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6")

    for fameRepo in fameRepos:
        title = fameRepo.find('span', class_="repo").contents[0]
        content = ""
        
        try:
            content = fameRepo.find('p', class_="pinned-item-desc color-fg-muted text-small d-block mt-2 mb-3").contents[0].split("\n")[1].strip()
            if len(content) == 0:
                raise Exception("No Description Found")
        except:
            content = "No Description Found"

        # print(fameRepo)

        user = url.split('/')[1]
        image = "https://raw.githubusercontent.com" + user + "/{0}/master/images/banner.jpg"

        res['famousRepo'].append(
                {
                'title': title,
                'link': url + "/" + title,
                'content': content,
                'image': image.format(title)
                })

    return res

def itch_Scraper(url):
    r=re.get(url)
    htmlcontent=r.content

    soup=BeautifulSoup(htmlcontent,'html.parser')

    res = {}
    links = soup.find('div', class_="user_links").findAll('a')

    res['links'] = []

    for link in links:
        res['links'].append(link.get('href'))

    res['game'] = []
    games = soup.find_all('div', class_="game_cell")

    for game in games:

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

    return res