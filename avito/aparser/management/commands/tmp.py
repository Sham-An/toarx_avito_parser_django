from lxml import html
from lxml import etree
import requests

# url = 'http://books.toscrape.com/'
#
# # downloading the web page by making a request objec
# res = requests.get(url)
#
# # making a tree object
# tree = html.fromstring(res.text)
#
# # navingating the tree object using the XPath
# book_genres = tree.xpath("//ul/li/a[contains(@href, 'categ')]/text()")[0:60]
#
#
# # since the result is the list object, we iterate the elements,
# # of the list by making a simple for loop
# for book_genre in book_genres:
#     print (book_genre.strip())

url = 'https://www.avito.ru/rostovskaya_oblast_aksay/mototsikly_i_mototehnika?radius=100'
#
# # downloading the web page by making a request objec
res = requests.get(url)
#tree = html.etree(res)
#
# # making a tree object
tree = html.fromstring(res.text)
#book = tree.xpath(path_container)
#print(html.tostring(tree))
#
# # navingating the tree object using the XPath
path_container = '//div[@data-marker="item"]'#//@id'
path_container_id = './/div[@data-marker="item"]//@id'
path = '//div[@data-marker="item"]'
price = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//meta[@itemprop="price"]'

#book_genres = tree.xpath(path_container)#[0:60]
#print(book_genres.xpath('//@id'))#[0:60]
#book_genres = []
book = tree.xpath(path_container)
book_genres = book #.xpath('//@id')#[0:60]

print(book_genres)
#
#
index=1
# # since the result is the list object, we iterate the elements,
# # of the list by making a simple for loop
for book_genre in book_genres: #book_genres:
    print(index)
    print(etree.tostring(book_genre))
    #print(book_genre.strip())
    #print(book_genre.text)#.strip())
    print(book_genre[index])#.strip())


    index+=1
