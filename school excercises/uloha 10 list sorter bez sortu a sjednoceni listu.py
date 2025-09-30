list1=[5,3,7,1]
list2=[6,4,8,2]
finlist=[]
index1=0
index2=0
def minlist1(x):
    e=0
    for z in range(0, len(list1)):
        if list1[e] >= list1[z]:
            e=z
            x = e
        else:
            e+=1
    return(x)

def minlist2(x):
    e=0
    for z in range(0, len(list2)):
        if list2[e] >= list2[z]:
            e=z
            x = e
        else:
            e+=1
    return(x)
               
for i in range(0, len(list1) + len(list2)):
    if len(list1) != 0 and len(list2) != 0:
        index1 = minlist1(index1)
        num1 = list1[index1]
        index2 = minlist2(index2)
        num2 = list2[index2]
        if num1 < num2:
            finlist.append(num1)
            list1.pop(index1)
        if num1 > num2:
            finlist.append(num2)
            list2.pop(index2)
            
    if len(list1) != 0:
        index1 = minlist1(index1)
        num1 = list1[index1]
        finlist.append(num1)
        list1.pop(index1)
        
    if len(list2) != 0:
        index2 = minlist2(index2)
        num2 = list2[index2]
        finlist.append(num2)
        list2.pop(index2)
        
print(finlist)

    
        
    
