# merging  of two d array
l1=[[1,2,3],[4,5,6],[9,8,7]]
l2 =[[10,12,13],[14,15,16],[22,23,24]]
add =[]
for i in range(0,len(l1)):
    add=add+[l1[i]+l2[i]]
print(add)
