from PIL import ImageTk, Image
import requests, bs4, webbrowser, os, tkinter

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


#Code to fetch random comic, works the same as above
randomimgurl = ''
randomtitle = ''

randomreq = requests.get('https://c.xkcd.com/random/comic')
randomreq.raise_for_status()

randomsoup = bs4.BeautifulSoup(randomreq.text, 'html.parser')
randomurls = randomsoup.select('#comic img')

for i in randomurls:
    randomimgurl += 'https:' + i['src']
    for j in i['alt'].split(' '):
        randomtitle += j

randomimgreq = requests.get(randomimgurl)
randomimgreq.raise_for_status()

choice = input('Latest/Random (L/R):')
opencomic = input('Open comic once done downloading? (y/n):')
if choice == 'L':
    img = open(title, 'wb')
    for chunk in req2.iter_content(100000):
        img.write(chunk)
    if opencomic.lower() == 'y':
        webbrowser.open(os.path.abspath(title))
    img.close()
elif choice == 'R':
    img = open(randomtitle, 'wb')
    for chunk in randomimgreq.iter_content(100000):
        img.write(chunk)
    if opencomic.lower() == 'y':
        webbrowser.open(os.path.abspath(randomtitle))
    img.close()

# This line of shell does about the same thing:
# wget $(curl https://xkcd.com 2> /dev/null | grep -i "hotlinking" | grep -Eo 'https:[/|a-z|A-Z|\.|_]+?png' | head -n 1) &> /dev/null

class FullScreenWin():
    def __init__(self, master, **kwargs):
        self.master=master
        self._geom='200x200+0+0'
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        master.geometry("{0}x{1}+0+0".format(w, h))
        master.bind('<Escape>',self.toggle_geom)
        
        pilImg = Image.open(title)
        pilImg = pilImg.resize((w, h), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(pilImg)
        canvas = tkinter.Canvas(master, width=w, height=h)
        canvas.pack()
        canvas.create_image(w/2, h/2, image=image)
        master.update_idletasks()
        master.update()

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root=tkinter.Tk()
app=FullScreenWin(root)
root.mainloop()
