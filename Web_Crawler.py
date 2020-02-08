__author__ = 'KittipatDechkul'

import requests
from bs4 import BeautifulSoup

url = "https://theinternship.io/"
data = requests.get(url)

soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all("span",{"class":"list-company"})
c = soup.find_all("img",{"class":"center-logos"})
discription = list()
logo_pic = list()
ans = list()
Logo_url  = list()
n = 0
for i in x:
    discription.append(i.text)

for j in c:
    logo_pic.append(j.get('src'))
    n = n+1
for k in range(n):
    ans.append(logo_pic[k]+":"+discription[k])
    
ans.sort(key=len, reverse=True) 

for line in ans:
    Type = line.split(":")
    Logo_url.append(Type[0])


if __name__ == '__main__':
    print (*Logo_url,sep="\n")