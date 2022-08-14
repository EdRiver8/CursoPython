from urllib.request import urlopen
from bs4 import BeautifulSoup #pip install beautifulsoup4

# url = 'python.org/'
# response = urlopen('http://'+url)
# print(response.read(100))# 100 primeros datos de la pagina

# response2 = urlopen('http://google.com/')
# for line in response2:
#     print(line.rstrip())# remueve los espacios en blanco al final de la cadena
    
url = input("Ingresa la direccion de la cual obtener los links: ")
response3 = urlopen('https://'+url)
print(type(response3))
soup = BeautifulSoup(response3)
for link in soup.find_all('a'):
    print(link.get('href'))