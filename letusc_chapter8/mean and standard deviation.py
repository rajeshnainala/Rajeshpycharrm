import array as arr
import math
a=arr.array('i',[-6,-12,8,13,11,6,7,2,-6,-9,-10,11,10,9,2])
sum=0
for i in range(len(a)):
    sum+=a[i]
mean=sum/len(a)
def standard_deviation(c):
    sum_sd=0
    for i in range(len(c)):
        k=math.pow(c[i]-mean,2)
        sum_sd+=k
    variance=sum_sd/len(c)
    standard=math.sqrt(variance)
    print("the standard deviation of data is: ",standard)
print("the mean of data is: ",mean)
standard_deviation(a)
