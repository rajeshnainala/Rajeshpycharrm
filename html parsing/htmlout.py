from bs4 import BeautifulSoup
file=open("basicc.html","r")
soup=BeautifulSoup(file,"html.parser")
#print(soup.prettify())
c=input("enter the tag")
d=c.split(".")
#print(soup.find_all(d[0]))
#body.student.sname

for i in d:
    soup=soup.find(i)
    if soup==None:
        flag=1
        break
if flag==1:
    print("tag is invalid")
else:
    print(soup.text)






