import json
from logging import getLogger
#from aparser.models import Category
#from aparser.models import Category
#from aparser.models import Region
#from aparser.models import City
# from logging import getLogger
# from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError

logger = getLogger(__name__)


def category_add(id):
    #models = Category
    #cat = Category.get(pk=id)
    print(id)

# #
# #  #   PAGE_LIMIT = 10
# #      try:
# #         p = Category.objects.get(url=url)
# #         p.task = self.task
# #         p.title = title
# #         p.price = price
# #         p.currency = currency
# #         p.save()
# #     except Product.DoesNotExist:
#         p = Category(
#             pk = pk,
#             name = name,
#             parent_Id = parent_Id,
#             JsId = JsId,
#             # task=self.task,
#             # url=url,
#             # title=title,
#             # price=price,
#             # currency=currency,
#             # published_date=date,
#         ).create()
#
#     logger.debug(f'product {p}')


def list_dict(dicts):

    print("__РЕКУРСИЯ___111_LIST_DICT_111_____")
    for k, v, in dicts.items():
    #for k, v in data:

        try:
            print("key:\t" + k)
            list_dict(v)
        except AttributeError:
            print("value:\t" + str(v))
            print(type(v))


def list_category(data):
    all_id = []
    print("___________22 LIST_DICT 22________________")
    for dataitems in data['categories']:
        print(dataitems['id'], dataitems['name'])
        print(dataitems)
        all_id.append(dataitems['id'])
        #print(type(dataitems['id']))

        if dataitems['id']>0 :
            for datainfo in dataitems['children']:
                if datainfo['id'] in all_id:
                    print('IIIIDDDD Поймали ДУБЛЯЖ')
                    break
                all_id.append(datainfo['id'])
                #if 'Ипот' in datainfo['name']:
                #    print('Поймали ИПОТЕКУ')
                # break
                id=datainfo['id']
                name = datainfo['name']
                parentId = datainfo['parentId']
                print(id, name, parentId)
                #print(datainfo['id'], datainfo['name'], datainfo['parentId'])
                category_add(id)
    all_id.sort()
    print(all_id)
       #except AttributeError:

def list_region(data):
    all_id = []
    print("___________22 LIST_CATEGORY 22________________")
    for dataitems in data['data']:
        print(dataitems['id'], dataitems['name'])
        #        print(dataitems)
        #all_id.append(dataitems['id'])
        if dataitems['id'] in all_id:
            print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
            break
        all_id.append(dataitems['id'])
        # if 'Ипот' in datainfo['name']:
        #    print('Поймали ИПОТЕКУ')
        # break
        print(dataitems['id'], dataitems['name'])
    all_id.sort()
    print(all_id)
       #except AttributeError:

def list_city(data):
    all_id = []
    print("___________22 LIST_CATEGORY 22________________")
    for dataitems in data['data']:
        #print(dataitems['id'], dataitems['name'])
        #        print(dataitems)
        #all_id.append(dataitems['id'])
        if dataitems['id'] in all_id:
            print('IIIIDDDD Поймали ДУБЛЯЖ!!!!!!!!!!!!!!!!!!!!!')
            break
        all_id.append(dataitems['id'])
        # if 'Ипот' in datainfo['name']:
        #    print('Поймали ИПОТЕКУ')
        # break
        print(dataitems['id'], dataitems['name'], dataitems['parent_Id'])
    all_id.sort()
    print(all_id)
       #except AttributeError:



def Open_json_category():

    with open("avito_category.json", encoding='utf-8') as file:
        data = json.load(file)
        #list_dict(data)
        list_category(data)
        #print(data)


def Open_json_region():

    with open("avito_region.json", encoding='utf-8') as file:
        data = json.load(file)
        #list_dict(data)
        list_region(data)
        #print(data)


def Open_json_city():
    with open("avito_city.json", encoding='utf-8') as file:
        data = json.load(file)
        # list_dict(data)
        list_city(data)
        # print(data)


if __name__ == '__main__':
    Open_json_category()
    #Open_json_region()
    #Open_json_city()