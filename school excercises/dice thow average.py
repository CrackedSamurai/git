import math
import random

dicetype = int(input("dice type:"))
amountofdices = int(input("amount of dices:"))
throws = int(input("amount of throws:"))
resultlist = []
diction = {}

def num(dices, dicetype):
    result = 0
    while dices != 0:
        dices -= 1
        result += random.randint(1, dicetype)
        #print(result)
    return result
    

for x in range(0, throws):
    resultlist.append(num(amountofdices, dicetype))
    #print(resultlist)

for num in resultlist:
    amount = resultlist.count(num)
    while num in resultlist:  resultlist.remove(num)
    diction.update({num: amount})
    
sorteddiction = sorted(diction.items(), key=lambda x:x[0])
print(sorteddiction)
