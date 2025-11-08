import requests

from bs4 import BeautifulSoup 


baseurl='https://www.nseindia.com/'

headerColle={
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070213 BonEcho/2.0.0.2pre'
}

params = {
    "symbol": "ADANIPORTS"
}


print('tedst1')
r=requests.get(baseurl,headers=headerColle)
print('test2')


# print(r.content)

soup=BeautifulSoup(r.content,features="lxml")
# print(soup)

print(soup.find(class_='stockPreviousClose'))