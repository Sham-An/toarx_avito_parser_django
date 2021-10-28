
    # В этом случае нам повезло, потому что все эти тексты содержат ключевое слово. Все они начинаются со слова «use». Чтобы захватить их, мы напишем следующее выражение:
    #
    # tree.xpath('//p[contains(text(),"Use")]/text()')
    # Давайте разберем, что мы видим:
    #
    # [] - вы можете видеть, что часть выражения заключена в квадратные скобки. Это называется «предикатом» и используется для фильтрации узлов на основе критериев, указанных внутри него. В этом случае он будет отфильтровывать узлы, которые обычно выводит «//p».
    # contains() - это ищет первый аргумент для случаев, когда второй аргумент присутствует. В этом случае мы ищем весь текст с надписью «use».

# for item in tree.xpath('//div[@class="element"]'):
#     name = item.xpath('./div[@class="name"]/text()')
#     description = item.xpath('./div[@class="description"]/text()')

# https://habr.com/ru/post/280238/
#Полный код для парсинга html-файлов под катом
import requests
from bs4 import BeautifulSoup
from lxml import html

    #Еще небольшой хинт для debug'a: для того, чтобы посмотреть,
    # что внутри выбранной ноды в BeautifulSoup можно просто распечатать ее,
    # а в lxml воспользоваться функцией tostring() модуля etree.

    # BeatifulSoup
    #print item

    #lxml
    #from lxml import etree
    #print etree.tostring(item_lxml)
    # ИЛИ
    #text = etree.tostring(element, method='text', encoding='utf-8')
    #if strip:
    #    text = text.strip()
    #return str(text, encoding='utf-8')

s = requests.Session()
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })

def load_user_data(user_id, page, session):
    url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/%d/#list' % (user_id, page)
    request = session.get(url)
    return request.text

def contain_movies_data(text):
    soup = BeautifulSoup(text)
    film_list = soup.find('div', {'class': 'profileFilmsList'})
    return film_list is not None

# loading files
page = 1
while True:
    user_id = 17376500
    data = load_user_data(user_id, page, s)
    if contain_movies_data(data):
        with open('./page_%d.html' % (page), 'w') as output_file:
            output_file.write(data.encode('cp1251'))
            page += 1
    else:
            break

user_id = 17376500 #12345
url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
#http://www.kinopoisk.ru/user/17376500/votes/list/ord/date/page/2/#list
r = requests.get(url)
with open('test.html', 'w') as output_file:
  output_file.write(r.text)#.encode('cp1251'))
def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text

def parse_user_datafile_bs(filename):
    results = []
    text = read_file(filename)

    soup = BeautifulSoup(text)
    film_list = film_list = soup.find('div', {'class': 'profileFilmsList'})
    items = film_list.find_all('div', {'class': ['item', 'item even']})
    for item in items:
        # getting movie_id
        movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')
        movie_desc = item.find('div', {'class': 'nameRus'}).find('a').text
        movie_id = re.findall('\d+', movie_link)[0]

        # getting english name
        name_eng = item.find('div', {'class': 'nameEng'}).text

        #getting watch time
        watch_datetime = item.find('div', {'class': 'date'}).text
        date_watched, time_watched = re.match('(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2})', watch_datetime).groups()

        # getting user rating
        user_rating = item.find('div', {'class': 'vote'}).text
        if user_rating:
            user_rating = int(user_rating)

        results.append({
                'movie_id': movie_id,
                'name_eng': name_eng,
                'date_watched': date_watched,
                'time_watched': time_watched,
                'user_rating': user_rating,
                'movie_desc': movie_desc
            })
    return results

def parse_user_datafile_lxml(filename):
    results = []
    text = read_file(filename)

    tree = html.fromstring(text)

    film_list_lxml = tree.xpath('//div[@class = "profileFilmsList"]')[0]
    items_lxml = film_list_lxml.xpath('//div[@class = "item even" or @class = "item"]')
    for item_lxml in items_lxml:
        # getting movie id
        movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]
        movie_desc = item_lxml.xpath('.//div[@class = "nameRus"]/a/text()')[0]
        movie_id = re.findall('\d+', movie_link)[0]

        # getting english name
        name_eng = item_lxml.xpath('.//div[@class = "nameEng"]/text()')[0]

        # getting watch time
        watch_datetime = item_lxml.xpath('.//div[@class = "date"]/text()')[0]
        date_watched, time_watched = re.match('(\d{2}\.\d{2}\.\d{4}), (\d{2}:\d{2})', watch_datetime).groups()

        # getting user rating
        user_rating = item_lxml.xpath('.//div[@class = "vote"]/text()')
        if user_rating:
            user_rating = int(user_rating[0])

        results.append({
                'movie_id': movie_id,
                'name_eng': name_eng,
                'date_watched': date_watched,
                'time_watched': time_watched,
                'user_rating': user_rating,
                'movie_desc': movie_desc
            })
    return results