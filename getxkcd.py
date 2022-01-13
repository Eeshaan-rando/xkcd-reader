import requests, bs4

#Download the main xkcd page
req1 = requests.get('https://xkcd.com')
req1.raise_for_status()

#Generate bs4 object
xkcdsoup = bs4.BeautifulSoup(req1.text, 'html.parser')

#Extract image URL and image file title
imgurl = ''
title = ''
urls = xkcdsoup.select('#comic img')
for i in urls:
    imgurl += 'https:' + i['src']
    for j in i['alt'].split(' '):
        title += j

#Download image content from image URL
req2 = requests.get(imgurl)
req2.raise_for_status()

#Write to image file
img = open(title, 'wb')
for chunk in req2.iter_content(100000):
    img.write(chunk)
img.close()
