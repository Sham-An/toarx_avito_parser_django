import time
import io
import requests
from urllib.request import urlopen
import lxml.html
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
from random import randint
from urllib.request import urlopen
import threading
#index = 1
################ VARNING!!!!!!!!!!!!!!

#какой скрипт отрабатывает В Chrome Dev Tools: Elements → Right Click на элементе → Break On... → Attributes Modifications. Дальше вызвать поворот, и посмотреть какой скрипт полезет менять аттрибуты элемента.
#функции https://xsltdev.ru/xpath/

    # #       Beautiful Soup
    # soup = BeautifulSoup(text)
    # film_list = soup.find('div', {'class': 'profileFilmsList'})
    #
    # #           lxml
    # tree = html.fromstring(text)
    # film_list_lxml = tree.xpath('//div[@class = "profileFilmsList"]')[0]

    # #        Beatiful Soup
    # movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')
    # movie_desc = item.find('div', {'class': 'nameRus'}).find('a').text
    #
    # #          lxml
    # movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]
    # movie_desc = item_lxml.xpath('.//div[@class = "nameRus"]/a/text()')[0]

# for item in tree.xpath('//div[@class="element"]'):
#     name = item.xpath('./div[@class="name"]/text()')
#     description = item.xpath('./div[@class="description"]/text()')


    # Еще небольшой хинт для debug'a: для того, чтобы посмотреть, что внутри выбранной ноды в BeautifulSoup можно просто распечатать ее, а в lxml воспользоваться функцией tostring() модуля etree.
    # # BeatifulSoup
    # print item
    #
    # #lxml
    # from lxml import etree
    # print etree.tostring(item_lxml)

    
#БЕЗ BeautifulSoup

# Debag part 2 переменные https://youtu.be/HpJYVIRuQbU
# Debag part 3 изменение брекпоинтов на принт https://youtu.be/QA_aGDIHakA
# Condition условие остановки если (переменная >= )
# Evaluate and log вывод в консоль строки формата f" текст {переменная}  "
#https://youtu.be/n6x1pzlRK8A?t=1784 (30:43)

def parse_from_stars(url):
    url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html = requests.get(url, headers=headers)
    html_lxml = lxml.html.fromstring(html.content)
    #html = response.text
    print(f'html_lxml  {html_lxml}')
    # s = 'C:/tmp/star_wars_html.html'
    # local = s.encode('UTF-8')
    # with open(local, 'w',) as f:
    #     f.write(html)
    # #
    # # # read local html file and set up lxml html parser
    # #local = "C:\Python3\pythonProjects\avito_parser_django\avito\aparser\management\commands\star_wars_html.html"
    # s = 'C:/tmp/star_wars_html.html'
    # local = s.encode('UTF-8')
    # #local = 'C:/tmp/star_wars_html.html'

    #response = urlopen(local)
    #htmlparser = etree.HTMLParser()
    tree = etree.fromstring(html, etree.HTMLParser())
    index = 1

    for item in tree.xpath('//p/strong/text()'):
        # name = item.xpath('//meta[@itemprop="description"')
        # description = item.xpath('//div[substring(@class,1,13) ="iva-item-text"]')
        #print(name, description)
        index +=1
        print(index)
        print(etree.tostring(item))

    #tree = etree.parse(html, htmlparser)
    #tostr=etree.tostring(tree)
    #tree2= etree.parse(html, htmlparser)
    #print(tree2)
    return

def parse_xml(url):
    #https://habr.com/ru/post/280238/
    #url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
    headers = {'Content-Type': 'text/html', }
    response = requests.get(url, headers=headers)
    html_txt = response.text
    doc = lxml.html.fromstring(response.content)
#    print(doc)
    new_releases = doc.xpath('//div[@elementtiming="bx.catalog.container"]')[0]
#   print(new_releases)
    items_id = new_releases.xpath('.//div[@data-item-id]')  # , smart_strings=False) #.decode('utf8')
    meta_items_id = new_releases.xpath('.//meta[@itemprop="description"]/@content')  # , smart_strings=False)
    print(f'meta_items_id {meta_items_id[0]}')
    print(f'ВСЕГО {len(items_id)} В {items_id}')
    titles = new_releases.xpath('.//div[substring(@class,1,13) ="iva-item-desc"]//text()')
    prices = new_releases.xpath('.//div[@data-item-id]//meta[@itemprop="price"]/@content')
    ##all_in_one = new_releases.xpath('//*[//div[@data-item-id]//div[@data-marker="item-date"]//preceding::div[@data-marker="item-line"]]')
    print(len(titles))
    print(len(prices))

    # results = []
    # resp = requests.get(url, headers=headers)
    # text = resp.text
    # print("requests.get(url, headers=headers)")
    #
    # html_tree = html.fromstring(text)
    # print(html_tree)
    # Из окна с таблицей элементов выбор элементов
    # AVITO дерево группы

    path_old_bad = './/div[@elementtiming="bx.catalog.container"]//div[@data-marker="item"]' #//meta[@content]'
    path = './/div[@elementtiming="bx.catalog.container"]//div[@data-marker="catalog-serp"]'
    #path_title_bad = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@class = "iva-item-descriptionStep-QGE8Y"]//text()'
    path_title_long = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[substring(@class,1,13) ="iva-item-desc"]//text()'
    path_title = './/div[substring(@class,1,13) ="iva-item-desc"]//text()'
    path_description_long = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//meta[@itemprop="description"]'
    path_description = './/meta[@itemprop="description"]'
    # preceding-sibling
    path_name_long        = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//h3[@itemprop="name"]'
    path_name = './/h3[@itemprop="name"]'

    path_price_long = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//meta[@itemprop="price"]'
    path_price = './/meta[@itemprop="price"]'
    path_trader_long = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//a'
    path_trader = './/div[@data-marker="item-line"]//a/text()'
    # preceding-sibling
    #path_descrip_full = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//preceding-sibling::div[1]//div/text()'
    path_descrip = './/preceding-sibling::div[1]//div/text()'

    ##!!!!!!!####!!!!!!###!!!!#БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА
    # substring(@class,1,13) ="iva-item-text"
    path_descrip_full = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[substring(@class,1,13) ="iva-item-text"]'
    # path_descrip_full_text ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[substring(@class,1,13) ="iva-item-text"]//text()'

    # //h1[contains(text(),’ Log in to’)] Когда если известна часть постоянно видимого текста или атрибута. https://habr.com/ru/company/otus/blog/533354/
    # path_descrip_full_text ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[contains(@class,"iva-item-text")]//text()'

    # //h1[starts-with(text(),’Log in ’)] если известна ПЕРВАЯ часть постоянно видимого текста или атрибута.
    # path_descrip_full_text = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[starts-with(@class,"iva-item-text")]//text()'

    # starts-with(string, string) https://habr.com/ru/company/otus/blog/533354/
    path_descrip_full_text = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[starts-with(@class,"iva-item-text")]//text()'
    path_descrip = './/div[starts-with(@class,"iva-item-text")]//text()'
    path_time_old = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-date"]/text()'
    # following-sibling
    path_location = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//following-sibling::div[2]//span'

    # tree = html.fromstring(text)
    #
    # film_list_lxml = tree.xpath('//div[@class = "profileFilmsList"]')[0]
    # items_lxml = film_list_lxml.xpath('//div[@class = "item even" or @class = "item"]')
    # for item_lxml in items_lxml:
    path_container = './/div[@elementtiming="bx.catalog.container"]//div[@data-marker="catalog-serp"]'
    path_item = './/div[@data-marker="item"]'

    #tree = etree.fromstring(html, etree.HTMLParser())
    #tree = etree.fromstring(html_txt, etree.HTMLParser())
    #print(html_txt)
    tree = html.fromstring(html_txt)
    #tree = etree.fromstring(html)
    index = 1
    list_lxml = tree.xpath(path_container)[0]
    #list_lxml = tree.xpath(path_container)[0:9]
    #print(list_lxml)
    items = list_lxml.xpath(path_item)
    #print(items)
    #print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!etree.tostring(tree) {etree.tostring(tree)}')
    #for item in items:
    for item in tree.xpath(path): #.getall():

        print(item)
        item_id=item.xpath(".//@id")

        print(f'ITEM_ID {item.xpath(".//@id")[0]} type{type(item_id)}')
        #print(f'ITEM_ID {etree.tostring(item.xpath("//@id"))}')
        name = "NAME"
        name = item.xpath(path_title)[0]
        print(f'!!!!!!!!!!!!NAME {name}')
        index += 1
        description =""
        #description = item.xpath('//div[substring(@class,1,13) ="iva-item-text"]//text()')
        title = item.xpath('.//div[@class="iva-item-descriptionStep-QGE8Y"]//text()')[0]

        #description = item.xpath('./div[@class="description"]/text()')
        if index < 10:
            #print(etree.tostring(item), name, description)
            print(f' title = {title}')
            #index +=1
            #print(index)


    # list_lxml = tree.xpath(path)[0]
    # items_lxml = list_lxml.xpath('//div[@class = "iva-item-descriptionStep-QGE8Y"]//text()')
    # for item_lxml in items_lxml:
    #     desript = item_lxml.xpath('//meta[@itemprop="description"]')
        #print(desript)
    #     # getting movie id
    #     movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]



class OlxParser:

    def __init__(self, base_url):
        self.base_url = base_url
        print(base_url)
        #self.last_time =

    def get_page(self):

        try:
            res = requests.get(self.base_url)
            print(res)
        except requests.ConnectionError:
            return


        if res.status_code < 400:
            return res.content

    def get_last_offer(self, html):
        #print(f'!!!!!!!!!!!!!!!!!!!!!HTML {html}')
        html_tree = html.fromstring(html)
        #html_tree = lxml.html.fromstring(html)
        #Из окна с таблицей элементов выбор элементов
        #AVITO дерево группы
        #path =  './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[2]//a[@itemprop="url"]'
        #path = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id and @id]'
        path_container = './/div[@elementtiming="bx.catalog.container"]'
        path_item = './/div[@data-marker="item"]'
        path = './/div[@elementtiming="bx.catalog.container"]//div[@data-marker="item"]'

        path_title ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@class = "iva-item-descriptionStep-QGE8Y"]//text()'
        #//li[@class ^='ajax_block_product']  #substring('123456', 1, 3) = '123' substring()='iva-item-content'
        path_description = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//meta[@itemprop="description"]'
        #preceding-sibling
        path_price =       './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//meta[@itemprop="price"]'
        path_trader =      './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//a'
        # preceding-sibling
        path_descrip_full = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//preceding-sibling::div[1]//div'

##!!!!!!!####!!!!!!###!!!!#БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА
        #substring(@class,1,13) ="iva-item-text"
        path_descrip_full ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[substring(@class,1,13) ="iva-item-text"]'
        #path_descrip_full_text ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[substring(@class,1,13) ="iva-item-text"]//text()'

        #//h1[contains(text(),’ Log in to’)] Когда если известна часть постоянно видимого текста или атрибута. https://habr.com/ru/company/otus/blog/533354/
        # path_descrip_full_text ='.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[contains(@class,"iva-item-text")]//text()'

        #//h1[starts-with(text(),’Log in ’)] если известна ПЕРВАЯ часть постоянно видимого текста или атрибута.
        #path_descrip_full_text = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[starts-with(@class,"iva-item-text")]//text()'

        # starts-with(string, string) https://habr.com/ru/company/otus/blog/533354/
        path_descrip_full_text = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[starts-with(@class,"iva-item-text")]//text()'
        path_time_old =    './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-date"]'
        # following-sibling
        path_location =    './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[@data-marker="item-line"]//following-sibling::div[2]//span'
        #//div[contains(concat(' ', normalize-space(@class), ' '), ' iva-item-descriptionStep ')]

        offers = html_tree.xpath(path)

        #for offer in offers:
        # //*[@id="i2269555802"]/div/div[2]/div[6]/div/text()
        #print(offers[1].text)
        #print(etree.tostring(offers))
 #############################################################
        #Пробуем BeautifulSoup
        soup = BeautifulSoup(html,features="lxml")
        #print(soup.prettify())
        #for lnk in soup.find_all('a'):
        #    print("prn lnk ", lnk.get('href'))

        #print("prn text ", soup.get_text())

##############################################################
        last_offer = str(offers[1]) #last_offer.text_content()
        #last_offer_text_content = last_offer.text_content()
        #print(f'LastOffer {last_offer}   last_offer_text_content')
        #url_last=html_tree.xpath(path).get('href')

        url_last = str('https://www.avito.ru')+html_tree.xpath(path)[1].get('href')

        #print(f'Offers {len(offers)},{html_tree}, {url_last}') # offers)
        print(len(offers), html_tree, url_last)  # offers)

        try:
            last_offer = html_tree.xpath(path)[1]
            #print(last_offer.text_content())#https://youtu.be/n6x1pzlRK8A?t=1763
            #link = last_offer.xpath('.//a')[1].get('href') #Берем из элемента last [1] второй элемент и получаем из него ссылку на описание
            #link = last_offer.xpath(path).get('href')  # Берем из элемента last [1] второй элемент и получаем из него ссылку на описание
            link = url_last

            #Забираем время объявления
            ##time_node = last_offer.xpath('.//table/tbody/tr[2]//p/text')[2]
            ##cur_time = time_node.strip()[-5:] #берем последние 5 символов и убираем пробелы
            #print(link)
        except (IndexError, AttributeError):
            return
        #
        # if self.last_time != cur_time:
        #     self.last_time = cur_time
        #     print(cur_time, link)

    def run(self): # https://youtu.be/n6x1pzlRK8A?t=2651
        while True:
            page = self.get_page()
            #print(f'page  {page}')
            index = randint(2, 150)
            print(f'index = {index}')
            if page is None:
                time.sleep(2)
                continue

            self.get_last_offer(page)
            time.sleep(1)
            time.sleep((randint(6, 14)) if index % 10 != 0 else randint(10, 20))
            #index += 1


if __name__=="__main__":

    ##url_='https://www.olx.ua/list/'
    #url = 'https://www.avito.ru/rostov-na-donu/zapchasti_i_aksessuary'
    #url = 'https://www.avito.ru/rostov-na-donu/gruzoviki_i_spetstehnika?radius = 100'
    url = 'https://www.avito.ru/rostov-na-donu/mototsikly_i_mototehnika/mopedy_i_skutery-ASgBAgICAUQ82gE?f=ASgBAgECAUQ82gEBRcaaDBZ7ImZyb20iOjMwMCwidG8iOjcwMDB9&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80&radius=100'
    ##url='https://www.olx.ua/transport/'
    ##url_2 = 'https://www.olx.ua/nedvizhimost/'
    #parser = OlxParser(url)

    #parse_from_stars(url)
    parse_xml(url)
    ##parser_2 = OlxParser(url_2)
    #parser.run() #выключил для многопоточности

    # https://youtu.be/n6x1pzlRK8A?t=3264 многопоточность
    #t1 = threading.Thread(target=parser.run)
    #t2 = threading.Thread(target=parser_2.run)


