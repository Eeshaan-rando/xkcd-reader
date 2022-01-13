import requests, bs4 

#Use requests to download the main page to extract the URL of the image of the latest comic.
req1 = requests.get('https://xkcd.com')
req1.raise_for_status()

#Generate bs4 object that can be parsed for HTML tags
xkcdsoup = bs4.BeautifulSoup(req1.text, 'html.parser')

#Extract all the information within <meta ...> stuff
urls = xkcdsoup.select('meta')

title = ""
imgurl = ""

#Unpack the attributes dictionaries into a bunch of stuff that has the image url as an element
urllist = []
for i in urls:
    for j in i.attrs:
        urllist.append(str(i.attrs[j]))

#Get the image url and title from urllist 
for i in urllist:
    if "https://imgs.xkcd.com/comics/" in i:
        imgurl += i
m = imgurl[29:].split('_')
m.remove('2x.png')
for i in m:
    title += i[0].upper() + i[1:]

#Use requests to download the image from the image URL
req2 = requests.get(imgurl)
req2.raise_for_status()

#Create the image file and write the data to it
img = open(title, 'wb')
for chunk in req2.iter_content():
    img.write(chunk)
img.close()
