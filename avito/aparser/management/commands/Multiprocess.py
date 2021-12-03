import requests
import multiprocessing
from bs4 import BeautifulSoup
from lxml import html
import os
from random import randint
from fake_useragent import UserAgent
import time

def avito_prox(prox):
    url_ica = "http://icanhazip.com"
    url_avito="https://www.avito.ru/"

    UA1 = (f'{UserAgent().random}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
   #print(type(headers))
   #{'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    headers = {
        'User-Agent': UA1
    }

    htmdoc = "HTML"
    #    print('parent process:', os.getppid())
    print(f'                  process id:                                   {os.getpid()} \n')
    htmerr ="<title>Доступ"
    #<script nonce="4EfHAa+Wewtw9ulfxtc8VA==">   window.dataLayer = null;
    htmok="Авито: недвижимость, транспорт"

    try:
        time.sleep(1)
        time.sleep(randint(6, 14)) #if index % 10 != 0 else 20)
        response = requests.get(url_avito, headers=headers, proxies=prox, timeout=4).text
       # print(f"                                    !!!!!               {response.ok} {response.status_code}")
        if htmerr in response[:500]: #.upper():
            print(f"ПППОООППАААДДДОООССС {prox}\n {response[:500]}")
        elif htmok in response[:500]: #.upper():
        #else:
            print(f'IP_ICA: {response[:900]} " СРАБОТАЛ ПРОКСИ" {prox} \n {headers}')
            #{response.strip()}
            # resp_ica = requests.get(url=url_ica, headers=headers, proxies=prox)
            # html_txt = resp_ica.text
            # tree = html.fromstring(html_txt)
            # path_id = '//pre/text()'
            # print(f'XML {html_txt}')
    except:
        print(f'Прокси не валидный! {prox} \n {headers}')

    # print(f'MyIp prox prox {prox}')
    # link = "http://icanhazip.com"
    # url_ica = "http://icanhazip.com"
    #
    # resp_ica = requests.get(url=url_ica, headers=headers, proxies=prox)
    # html_txt = resp_ica.text
    # tree = html.fromstring(html_txt)
    # path_id = '//pre/text()'
    # print(f'XML {html_txt}')



def myip_ica(prox):
    url_ica = "http://icanhazip.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    htmdoc = "HTML"
    #    print('parent process:', os.getppid())
    print(f'                  process id:                                   {os.getpid()} \n')

    try:
        response = requests.get(url_ica, headers=headers, proxies=prox, timeout=1).text
        if htmdoc in response.upper():
            print("ПППОООППАААДДДОООССС")
        else:
            print(f'IP_ICA: {response.strip()} " СРАБОТАЛ ПРОКСИ" {prox} \n')
            # resp_ica = requests.get(url=url_ica, headers=headers, proxies=prox)
            # html_txt = resp_ica.text
            # tree = html.fromstring(html_txt)
            # path_id = '//pre/text()'
            # print(f'XML {html_txt}')
    except:
        print(f'Прокси не валидный! {prox}')

    # print(f'MyIp prox prox {prox}')
    # link = "http://icanhazip.com"
    # url_ica = "http://icanhazip.com"
    #
    # resp_ica = requests.get(url=url_ica, headers=headers, proxies=prox)
    # html_txt = resp_ica.text
    # tree = html.fromstring(html_txt)
    # path_id = '//pre/text()'
    # print(f'XML {html_txt}')


def myip(prox):
    #print(f'MyIp today {prox}')

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }
    htmdoc = "HTML"
    url_today = 'https://2ip.ru'

    try:
        response2 = requests.get(url=url_today, proxies=prox, timeout=2)
        soup = BeautifulSoup(response2.text, 'lxml')

        ip = soup.find('div', class_='ip').text.strip()
        location = soup.find('div', class_='value-country').text.strip()
        print(f'IP_Today: {ip}\nLocation: {location}')

    except:
        print(f'TODAY Прокси не валидный! {prox} \n {prox}')


def handler(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}',
    }

    # 1
    #myip(proxies)
    #myip_ica(proxies)
    avito_prox(proxies)


#    try:
#        response = requests.get(link, proxies=proxies, timeout=5).text
#        if htmdoc in response.upper():
#            print("ПППОООППАААДДДОООССС")
#        else:
#            print(f'IP: {response.strip()}\n " ПРОКСИ СРАБОТАЛ " {proxies}')
# #           myip(proxies)
#    except:
#        print(f'Прокси не валидный! {proxies} \n {proxies}')
# 2
# try:
#     response2 = requests.get(url=url_today, proxies=proxies, timeout=2)
#     soup = BeautifulSoup(response2.text, 'lxml')
#
#     ip = soup.find('div', class_='ip').text.strip()
#     location = soup.find('div', class_='value-country').text.strip()
#     print(f'IP_Today: {ip}\nLocation: {location}')
#     myip(proxies)
#
# except:
#     print(f'TODAY Прокси не валидный! {proxies} \n {proxies}')

# 3
# url_today = 'https://2ip.ru'
# response2 = requests.get(url=url_today, headers=headers, proxies=proxies)
# soup = BeautifulSoup(response.text, 'lxml')
#
# ip = soup.find('div', class_='ip').text.strip()
# location = soup.find('div', class_='value-country').text.strip()
#
# print(f'IP_Today: {ip}\nLocation: {location}')


# with open('proxy') as file:
with open('proxies.txt') as file:
    proxy_base = "".join(file.readlines()).strip().split('\n')
    i=1
    print(f'PROXY base {proxy_base}\n I={i}\n')
    # PROXY https://hideip.me/ru/proxy/socks5list


# with multiprocessing.Poll(multiprocessing.cpu_count()) as process: #Запускайте не через Pool, а через Process
# Подскажие как сделать запросы асинхрнонными? Используйте aiohttp
# И ещё asyncio. Создаёшь контекст менеджер для тасков и запускаешь в многопотоке асинхронные функции asyncio.
# мультипроцессинг нужно вызывать через сравнение name == main, иначе он уйдет в рекурсию.
# мне помогло только это:
# def main():
#     with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
#         process.map(handler, proxy_base)
#
# if _name_ == '__main__':
#     main()
#    process.map(handler, proxy_base)

def main():
    # with Pool(5) as p:
    # with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    #with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    with multiprocessing.Pool(12) as process:
        process.map(handler, proxy_base)


if __name__ == '__main__':
    main()
