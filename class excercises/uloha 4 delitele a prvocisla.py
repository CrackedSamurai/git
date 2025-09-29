num = int(input("enter number:"))
notdivisible = True
divider = 0
dividerlist = []
for x in range(2, int(num)):
    if int(num) % x == 0:
        dividerlist.append(x)
        divider += 1
        notdivisible = False
if notdivisible == False:
    print("not a prime number,", divider + 2, "dividers")
    print("dividers: 1, 2, ",dividerlist)
if notdivisible:
    print("prime number, only 2 dividers")
