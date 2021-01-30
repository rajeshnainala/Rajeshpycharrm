import array as arr
import numpy as np
a=arr.array('d',[0.0])
b=arr.array('d',[0.0])
angle=arr.array('d',[0.0])
area=arr.array('d',[0.0])
for i in range(6):
    a[i]=float(input("enter a first side"))
    a.append(i)
    b[i]=float(input("enter second side"))
    b.append(i)
    angle[i]=float(input("enter the angle"))
    angle.append(i)
    area[i]=(0.5*a[i]*b[i]*np.sin(angle[i]))
    area.append(i)
a.pop()
b.pop()
angle.pop()
area.pop()
print(a)
print(b)
print(angle)
print(area)
max=0
for i in range(len(area)):
    if area[i]>max:
        max=area[i]
print("the largest traingle part  with area",max)

