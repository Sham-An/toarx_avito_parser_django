import json
# from aparser.models import Category
from aparser.models import Region
# from logging import getLogger
# from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError


class RegionAdd:

 #   PAGE_LIMIT = 10
    try:
        p = Region.objects.get(url=url)
        p.task = self.task
        p.title = title
        p.price = price
        p.currency = currency
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

    logger.debug(f'product {p}')


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

                print(datainfo['id'], datainfo['name'], datainfo['parentId'])
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

if __name__ == '__main__':
    #Open_json_category()
    Open_json_region()
