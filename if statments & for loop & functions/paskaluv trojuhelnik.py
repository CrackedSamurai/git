x = input("pocet")
y=int(x)+1
trojuhelnik=[]
memory=[1,1]
for i in range(0,int(x)):
    lst=[1,1]
    for x in range(0,i):
        num = memory[0+x] + memory[1+x]
        lst.insert(1,num)
    memory = lst
    trojuhelnik.append(memory)

stred=round((len(list(" ".join(map(str, trojuhelnik[len(trojuhelnik)-1]))))/2)+0.1)
print(" "*round(stred + 0.1) + "1")
for i in trojuhelnik:
    mezera=stred-round((len(list(" ".join(map(str, i))))/2)+0.1)
    print(" "*mezera, *i, sep =" ")
    y-=1