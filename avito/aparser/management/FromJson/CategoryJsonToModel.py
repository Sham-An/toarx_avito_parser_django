import json


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


def list_dict3(data):
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
                all_id.append(datainfo['id'])

                if 'Ипот' in datainfo['name']:
                    print('Поймали ИПОТЕКУ')
                    break

                print(datainfo['id'], datainfo['name'], datainfo['parentId'])
    all_id.sort()
    print(all_id)
       #except AttributeError:




def Open_json():
    with open("avito_category.json", encoding='utf-8') as file:
        data = json.load(file)
        list_dict(data)
        #list_dict2(data)
        list_dict3(data)
        #print(data)
    #for item in data['categories']:
    #    print(f"Сохраненный {item['id']} = {item['name']}")

#        for item in data['categories']['children']:
#            print(f"Сохраненный children {item['id']} = {item['name']}")


if __name__ == '__main__':
    Open_json()
