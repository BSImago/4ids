#downloads pictures from a 4chan thread and stores them in the directory the script was ran from
import bs4 as bs
import urllib.request
import re
import os
threadurl = input("paste the thread you want to save from.")
filename = input("what common name do you want to save this stack of images as?")
os.mkdir(filename)
os.chdir(os.getcwd() + "//" + str(filename))
print("downloading...")
req = urllib.request.Request(threadurl, headers={'User-Agent': 'Mozilla/5.0'})
thread = urllib.request.urlopen(req).read()

soup = bs.BeautifulSoup(thread, "lxml")

soupStr=str(soup)
picList=[]
checkList=[]


picFinder = re.compile("i\.4cdn\.org/\w+/\d{1,20}\.\w{3,4}")
findPic = re.findall(picFinder,soupStr)
picList.append(findPic)
pnum = 0
picList = picList[0]
def f2(picList): 
   # order preserving
   finalList = []
   for e in picList:
       if e not in finalList:
           finalList.append(e)
   return finalList
finalList = f2(picList)
   
for pic in finalList:
	pnum += 1
	freverse = pic[:-5:-1]
	ftype = freverse[::-1]
	urllib.request.urlretrieve("http://" + pic, filename + str(pnum) + ftype)

input("pics downloaded")
