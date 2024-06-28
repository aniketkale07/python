list1=[3,4,56,6,33,33,6,71,8,5,51,22]

length=len(list1)
print(length)

for i in range(length //2):
    temp=list1[i]
    list1[i]=list1[length-i-1]
    list1[length-i-1]=temp
    
print(list1)
    