from bs4 import BeautifulSoup
import urllib.request
sarkilist=[]
for i in range(1,5):
    url="https://www.numberone.com.tr/muzik/number-one-top-40/page/"+str(i)
    url_oku=urllib.request.urlopen(url)
    soup=BeautifulSoup(url_oku,'html.parser')
    a=soup.find_all("div",attrs={"class":"description-column"})
    for x in a:
        y=x.find_all("h2" and "a")
        sarkilist.append(str(y).split("=")[2].split(">")[0])
dosya=open("fenomen2.txt","w")
for sarki in sarkilist:
    dosya.write(sarki+"\n")
dosya.close()
