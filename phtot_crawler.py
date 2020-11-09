from bs4 import *
import requests as rq
import os

#enter the url to search for photot
req1=rq.get("https://www.pexels.com/")

#the way in which the web page is viewed
soup = BeautifulSoup(req1.text,"html.parser")


links=[]

#make the regular expression for the patter for the photos
x = soup.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
    links.append(img['src'])

os.mkdir('photos')
i=1

for index,img_link in enumerate(links):
    if i <= 10:
        img_data=rq.get(img_link).content
        with open("photos\\"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break
