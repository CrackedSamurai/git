print("znaky:")
text = input()
text_split = []
text_split[:] = text
finalni_text = []
list_znaku = ["!", "?", "*", "@", "#"]
text_znaku = ["vykřičník", "otazník", "hvěydička", "zavináč", "křížek"]
print(text_split)

for znak in text_split:
    if znak.isupper():
        finalni_text.append("velké písmeno")
    if znak.islower():
        finalni_text.append("malé písmeno")
    for x in list_znaku:
        if znak == x:
            finalni_text.append(text_znaku[list_znaku.index(x)])
    else:
        finalni_text.append("jiný znak")

print(finalni_text)
