from bs4 import BeautifulSoup
flag=0
file=open("basicc.html",'r')
soup=BeautifulSoup(file,"html.parser")
person=input(("enter the string"))
sdt=soup.find(string=person)
if sdt==None:
    flag=1

if flag==1:
    print("string entered is invalid")
else:
    p=sdt.find_parent()
    parent=p.find_parent()
    print("The id of a ",person,"is",parent.id.text)
    print("The grade of a ",person,"is",parent.percnt.text)