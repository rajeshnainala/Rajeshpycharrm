import array as arr
unsorted_array=arr.array('i',[3,-6,7,10,33,2,-9,-13,15])
max=unsorted_array[0]
min=unsorted_array[0]
for i in range(0,len(unsorted_array)):
    if max<unsorted_array[i]:
        max=unsorted_array[i]
    if min>unsorted_array[i]:
        min=unsorted_array[i]
print("the largest number in array is",max)
print("the smallest number in array is ",min)

