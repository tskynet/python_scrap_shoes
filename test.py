from bs4 import BeautifulSoup
import requests

#liste de 10 pages de chaussons ATM.

req = requests.get('https://planetgrimpe.com/categorie-materiels/chaussons/page/12/')
urlGetList = 'https://planetgrimpe.com/categorie-materiels/chaussons/page/'
# print('hello')
# incrementReq = True
# count = 1
# while incrementReq:
#     url = urlGetList + str(count) + '/'
#     req = requests.get(url)
#     # print('URL : ')
#     # print(url)
#     # print('counter:')
#     # print(count)
#     soup = BeautifulSoup(req.text, "html.parser")
#     soup.find_all('article', {'class': 'unmat'})
#     #si la page n'existe pas, on arrête la boucle.
#     if req.status_code == 404:
#         incrementReq = False
#         print('there is no more page to scrap.')
#     count = count + 1
# print(req.status_code)


r = requests.get('https://planetgrimpe.com/categorie-materiels/chaussons/')
print('hello')
# print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
test = soup.find_all('article', {'class' : 'unmat'})
# print(len(test))
# newsoup = BeautifulSoup(test[0], 'html.parser')
e = str(test[0].h1)
print(e.strip())
print(e.replace(' ', ''))


# mydivs = soup.find_all("div", {"class": "stylelistrow"})
