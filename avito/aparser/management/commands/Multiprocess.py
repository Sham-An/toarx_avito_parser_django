import requests
import  multiprocessing

from bs4 import BeautifulSoup



def handler(proxy):
    link = "http://icanhazip.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
    }

    proxies = {
        'http': f'http//{proxy}',
        'https': f'http//{proxy}',
    }

    try:
        response = requests.get(link, proxies=proxies, timeout=4).text
        print(f'IP: {response.strip()}')
    except:
        print(f'Прокси не валидный! {proxies}')

    url_today = 'https://2ip.ru'
    response = requests.get(url=url_today, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()

    print(f'IP_Today: {ip}\nLocation: {location}')





with open('proxy') as file:
    proxy_base = "".join(file.readlines()).strip().split('\n')
    print(f'PROXY {proxy_base}')
    #PROXY https://hideip.me/ru/proxy/socks5list

#with multiprocessing.Poll(multiprocessing.cpu_count()) as process: #Запускайте не через Pool, а через Process
    #Подскажие как сделать запросы асинхрнонными? Используйте aiohttp
    # И ещё asyncio. Создаёшь контекст менеджер для тасков и запускаешь в многопотоке асинхронные функции asyncio.
    #мультипроцессинг нужно вызывать через сравнение name == main, иначе он уйдет в рекурсию.
    #мне помогло только это:
    # def main():
    #     with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
    #         process.map(handler, proxy_base)
    #
    # if _name_ == '__main__':
    #     main()
#    process.map(handler, proxy_base)

def main():
        with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
            process.map(handler, proxy_base)

if __name__ == '__main__':
        main()

