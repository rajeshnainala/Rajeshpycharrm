import array as arr
b=arr.array('i',[2,4,6,7,8,9,5,3])
c=arr.array('i',[])
for i in reversed(range(len(b))):
    c.append(b[i])
print(c)
