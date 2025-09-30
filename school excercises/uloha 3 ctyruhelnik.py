def ctyruhelnik(x,y):
    strana1 = []
    strana2 = ["*", "*"]
    while x >= 1:
        print(x)
        x -= 1
        strana1.append("*")
        if x > 1:
            strana2.insert(1, " ")
    print(strana1)
    while y >= 1:
        y -= 1
        print(strana2)
    
    print(strana1)

def vykreslit(x,y):
    print("*" * x)
    for i in range(y):
        print("*" + " " * (x-2) + "*")
    print("*" * x)

x = int(input("x="))
y = -2 + int(input("y="))
ctyruhelnik(x,y)
vykreslit(x,y)



        
