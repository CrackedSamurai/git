meze = int(input("zadejte mezi"))
i = 2
zapis = [True for x in range(2, meze + 1)]


while i * i < meze:
    j=i-2
    while j < meze-i-1:
        j+=i
        zapis[int(j)] = False
    i+=1
print(zapis)
