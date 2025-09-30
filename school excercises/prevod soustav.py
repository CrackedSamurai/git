cislo = int(input("cislo"))
ze_soustava = int(input("puvodni soustava (max 10)"))
do_soustava = int(input("konecna soustava (max 36)"))
dessoustava = 0
output = ""


for x in str(cislo):
    dessoustava = (dessoustava + int(x)) * ze_soustava
dessoustava = int(dessoustava)/ze_soustava

while dessoustava > 0:
    zbytek = int(dessoustava % do_soustava)
    if zbytek >= 10:
        zbytek = chr(zbytek-10 + ord("A"))
    dessoustava = dessoustava // do_soustava
    output = str(zbytek) + output
print(output)
