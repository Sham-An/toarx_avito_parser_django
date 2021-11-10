import datetime
import urllib.parse
from logging import getLogger

import lxml.html
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
from random import randint

import bs4
import requests
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from aparser.constants import STATUS_NEW
from aparser.constants import STATUS_READY
from aparser.models import Product, Region, City
from aparser.models import Task
from aparser.models import Category
import json

#python manage.py parse_avito
logger = getLogger(__name__)

class CityGet:

    def list_city(self):

        with open("avito_city.json", encoding='utf-8') as file:
            data = json.load(file)

        all_id = []
        print("___________22 LIST_CATEGORY 22________________")
        for dataitems in data['data']:
            # print(dataitems['id'], dataitems['name'])
            #        print(dataitems)
            # all_id.append(dataitems['id'])
            if dataitems['id'] in all_id:
                print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
                break
            all_id.append(dataitems['id'])
            # if 'Ипот' in datainfo['name']:
            #    print('Поймали ИПОТЕКУ')
            # break
            id = dataitems['id']
            name = dataitems['name']
            parent_Id = dataitems['parent_Id']
            #reg = Region.objects.get(id=parent_Id)
            try:
                obj = City.objects.get(id=id)
            except City.DoesNotExist:
                obj = City(id=id, name=name, parent_Id=parent_Id)
                obj.save()


            #print(dataitems['id'], dataitems['name'], dataitems['parent_Id'])
        all_id.sort()
        print(all_id)
        # except AttributeError:


class RegionGet:

    def list_region(self):

        with open("avito_region.json", encoding='utf-8') as file:
            data = json.load(file)

        all_id = []
        print("___________22 LIST_CATEGORY 22________________")
        for dataitems in data['data']:
            print(dataitems['id'], dataitems['name'])
            #        print(dataitems)
            # all_id.append(dataitems['id'])
            if dataitems['id'] in all_id:
                print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
                break
            all_id.append(dataitems['id'])
            # if 'Ипот' in datainfo['name']:
            #    print('Поймали ИПОТЕКУ')
            # break
            id = dataitems['id']
            name = dataitems['name']

            try:
                obj = Region.objects.get(id=id)
            except Region.DoesNotExist:
                obj = Region(id=id, name=name)#, parentId=parentId)
                obj.save()

            #print(dataitems['id'], dataitems['name'])


        all_id.sort()
        print(all_id)


class CategoryGet:

    def find_category(self):
        obj = Category.objects.all() #filter(status=STATUS_NEW).first()
        print(obj)

    def list_category(self):

        all_id = []

        with open("avito_category.json", encoding='utf-8') as file:
            data = json.load(file)
        print("___________22 LIST_DICT 22________________")
        for dataitems in data['categories']:
            print(dataitems['id'], dataitems['name'])
            print(f'Родительские {dataitems}')
            all_id.append(dataitems['id'])
            id1 = dataitems['id']
            name = dataitems['name']
            parentId = 0
            try:
                 obj1 = Category.objects.get(id=id1)
            except Category.DoesNotExist:
                 obj1 = Category(id=id1, name=name, parentId=parentId)
                 obj1.save()

            #print(type(dataitems['id']))

            if dataitems['id']>0 :
                for datainfo in dataitems['children']:
                    if datainfo['id'] in all_id:
                        print('IIIIDDDD Поймали ДУБЛЯЖ')
                        break
                    all_id.append(datainfo['id'])
                    id = datainfo['id']
                    name = datainfo['name']
                    parentId = datainfo['parentId']
                    print(id, name, parentId)

                    try:
                        obj = Category.objects.get(id=id)
                    except Category.DoesNotExist:
                        obj = Category(id=id, name=name, parentId=parentId)
                        obj.save()
                    #print(datainfo['id'], datainfo['name'], datainfo['parentId'])
                    #category_add(id)
        all_id.sort()
        print(all_id)
           #except AttributeError:


class AvitoParserXPath:
    def __init__(self):
        print('ParserXPath222222222')
        self.session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
            'Content-Type': 'text/html',
        }
        print('ParserXPath 3')
        self.task = None

    def find_task(self):
        obj = Task.objects.filter(status=STATUS_NEW).first()
        tasks = Task.objects.filter(status=STATUS_NEW).all()
        #obj = Task.objects.filter(status=STATUS_NEW).all()
        print(f'tasks.query {tasks.query} \n {tasks}')
        # for ts in tasks:
        #     print(ts.title)
        #     obj = ts
        #     if not obj:
        #         raise CommandError('ParserXPath no tasks found!!!!')
        #     self.task = obj
        #     logger.info(f'ParserXPath Работаем над заданием {self.task}')

        # print(self)
        if not obj:
            raise CommandError('ParserXPath no tasks found!!!!')
        self.task = obj
        logger.info(f'ParserXPath Работаем над заданием {self.task}')

    def finish_task(self):
        self.task.status = STATUS_READY
        #self.task.save()
        logger.info(f'ParserXPath Завершили задание')

    def get_page(self, page: int = None):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
            'Content-Type': 'text/html',
        }
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page

        url = self.task.url
        #r = self.session.get(url, params=params)
        response = requests.get(url,  params=params, headers=headers)
        r = response #.text
        #r.raise_for_status()
        #print('!!!!!!!!!!!!!!!!!!!!!!! get_page')
        return r #.text



    def get_pagination_limit(self):
        text = self.get_page()
        #print(text)
        ##soup = bs4.BeautifulSoup(text, 'lxml')
        #
        # container = soup.select('a.pagination-page')
        # if not container:
        #     return 1
        # last_button = container[-1]
        # href = last_button.get('href')
        # if not href:
        #    return 1

        # r = urllib.parse.urlparse(href)
        # params = urllib.parse.parse_qs(r.query)
        # return min(int(params['p'][0]), self.PAGE_LIMIT)
        return 2

    def get_blocks(self, page: int = None):

        headers = {'Content-Type': 'text/html', }
        response = self.get_page(page=page)
        html_txt = response.text
        tree = html.fromstring(html_txt)

        path_item = '//div[@data-marker="item"]'
        path_id = ".//@id"
        path_name = './/h3[@itemprop="name"]/text()'
        #path_name_long = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//h3[@itemprop="name"]'

        path_description_meta = './/meta[@itemprop="description"]/@content'
        #//div[@data-marker="item"]//meta[@itemprop="description"]/@content
        #path_description_div = './div[@class="description"]/text()'
        path_description_div = './/div[substring(@class ,1, 13) ="iva-item-text"]//text()'

        index = 1

        for item in tree.xpath(path_item):  # .getall():
            #print(item)
            item_id = item.xpath(path_id)[0]
            print(f'ITEM_ID {item_id}') #{item.xpath(".//@id")[0]} type{type(item_id)} {item.xpath(path_id)[0]}')
            # name = item.xpath(path_title)[0]
            name = str(item.xpath(path_name)[-1])
            print(f'{index}!!!!!!!!!!!!NAME {name}')
            #index += 1
            description_div = "".join(item.xpath(path_description_div)) #join - список в строку
            LenDesk = len(description_div)
            #description_div = item.xpath(path_description_div)

            print(f' {index} description_div len = {LenDesk} \n  = {description_div}')
            index +=1
    #
        # # Запрос CSS-селектора, состоящего из множества классов, производится через select
        # #container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        # container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        # print(f'КОНТЕЙНЕР  {container}')
        # for item in container:
        #     self.parse_block(item=item)


    def parse_all(self):
        # Выбрать какое-нибудь задание
        #print('4')
        self.find_task()

        limit = self.get_pagination_limit()
        logger.info(f'ParserXPath !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Всего страниц: {limit}')

        for i in range(1, limit + 1):
             logger.info(f'XPath Работаем над страницей {i}')
             self.get_blocks(page=i)
        #
        # # Завершить задание
        # self.finish_task()



class AvitoParser:
    PAGE_LIMIT = 10
    print('NoXpath1111111111111111111')

    def __init__(self):
        print('NoXpath222222222')
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }
        print('NoXpath3')
        self.task = None

    def find_task(self):
        # print('5!!!!!!!!')
        # print(Task)
        obj = Task.objects.filter(status=STATUS_NEW).first()
        # print(self)
        if not obj:
            raise CommandError('no tasks found!!!!')
        self.task = obj
        logger.info(f'Работаем над заданием {self.task}')

    def finish_task(self):
        self.task.status = STATUS_READY
        self.task.save()
        logger.info(f'Завершили задание')

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page

        url = self.task.url
        r = self.session.get(url, params=params)
        r.raise_for_status()
        #print('!!!!!!!!!!!!!!!!!!!!!!! get_page')
        return r.text

    @staticmethod
    def parse_date(item: str):
        logger.debug('parse_date: %s', item)
        params = item.strip().split(' ')
        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days=1)
            else:
                logger.error('Не смогли разобрать день: %s', item)
                return

            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date=date, time=time)

        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map = {
                'января': 1,
                'февраля': 2,
                'марта': 3,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                logger.error('Не смогли разобрать месяц: %s', item)
                return

            try:
                today = datetime.datetime.today()
                time = datetime.datetime.strptime(time, '%H:%M')
                return datetime.datetime(day=day, month=month, year=today.year, hour=time.hour, minute=time.minute)
            except ValueError:
                year = datetime.datetime.strptime(time, '%Y')
                return datetime.datetime(day=day, month=month, year=year.year)

        else:
            logger.error('NoXpath Не смогли разобрать формат:', item)
            return

    def parse_block(self, item):
        # Выбрать блок со ссылкой
        url_block = item.select_one('a.snippet-link')
        if not url_block:
            raise CommandError('bad "url_block" css')

        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        # Выбрать блок с названием
        title = url_block.string.strip()
        if not title:
            raise CommandError(f'no title for item: {url_block}')

        # Выбрать блок с названием и валютой
        price_block = item.select_one('span.price')
        #print(f'Выбрать блок с названием и валютой {price_block}')
        if not price_block:
            raise CommandError('bad "price_block" css')

        price_block = price_block.get_text('\n')
        price_block = list(filter(None, map(lambda i: i.strip(), price_block.split('\n'))))
        if len(price_block) == 2:
            price, currency = price_block
            price = int(price.replace(' ', ''))
        elif len(price_block) == 1:
            # Бесплатно
            price, currency = 0, None
        else:
            price, currency = None, None
            logger.error(f'Что-то пошло не так при поиске цены: {price_block}, {url}')

        # Выбрать блок с датой размещения объявления
        date = None
        date_block = item.select_one('div.item-date div.js-item-date.c-2')
        if not date_block:
            raise CommandError('bad "date_block" css')

        absolute_date = date_block.get('data-absolute-date')
        if absolute_date:
            date = self.parse_date(item=absolute_date)

        try:
            p = Product.objects.get(url=url)
            p.task = self.task
            p.title = title
            p.price = price
            p.currency = currency
            print(f'NoXpath!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! try: p.save()')
            p.save()
        except Product.DoesNotExist:
            p = Product(
                task=self.task,
                url=url,
                title=title,
                price=price,
                currency=currency,
                published_date=date,
            ).save()
            print(f'NoXpath!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! except Product.DoesNotExist:')

        logger.debug(f'product {p}')

    def get_pagination_limit(self):
        text = self.get_page()
        soup = bs4.BeautifulSoup(text, 'lxml')

        container = soup.select('a.pagination-page')
        if not container:
            return 1
        last_button = container[-1]
        href = last_button.get('href')
        if not href:
            return 1

        r = urllib.parse.urlparse(href)
        params = urllib.parse.parse_qs(r.query)
        return min(int(params['p'][0]), self.PAGE_LIMIT)

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')
        #print(f'SOUP   {soup}')

        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        #container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        print(f'КОНТЕЙНЕР  {container}')
        for item in container:
            self.parse_block(item=item)

    def parse_all(self):
        # Выбрать какое-нибудь задание
        #print('4')
        self.find_task()


        limit = self.get_pagination_limit()
        logger.info(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Всего страниц: {limit}')

        for i in range(1, limit + 1):
            logger.info(f'Работаем над страницей {i}')
            self.get_blocks(page=i)

        # Завершить задание
        self.finish_task()


class Command(BaseCommand):
    help = 'Парсинг Avito'

    def handle(self, *args, **options):
        #reg = RegionGet()
        #reg.list_region()
        #city = CityGet()
        #city.list_city()
        #cat = CategoryGet()
        #cat.find_category()
        #cat.list_category()

        # p = AvitoParser()
        # p.parse_all()

        p = AvitoParserXPath()
        p.parse_all()


#def main():
    #p = AvitoParser()
    #p.parse_all()

#
# if __name__ == '__main__':
#     main()
