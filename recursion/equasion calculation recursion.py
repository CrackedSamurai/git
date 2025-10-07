mem_list = []
equ_list = []
symbols = ["+","-","*","/","(",")"]

def listisizing(equasion):
    for x in equasion:
        if x == " ":
            continue
        elif x.isdigit() or x == ".":
            mem_list.append(x)
        elif (y == x for y in symbols):
            inserting()
            equ_list.append(x)
        else:
            raise ValueError(f"neplatny priklad {equasion}")
    inserting()
    evaluating(equ_list)
    return equ_list[0]

def inserting():
    if mem_list:
        equ_list.append(''.join(mem_list))
        mem_list.clear()

def calculating(equasion, start, end, last_operation):
    global done
    done =  False
    for index in range(start, end):
        if done:
            return equasion
        elif equasion[index] == "*":
            #prnt(equasion, start, end, index)
            equasion[index-1:index+2] = [float(equasion[index-1]) * float(equasion[index+1])]
            fix(equasion, start, end, last_operation)
            break
        elif equasion[index] == "/":
            #prnt(equasion, start, end, index)
            equasion[index-1:index+2] = [float(equasion[index-1]) / float(equasion[index+1])]
            fix(equasion, start, end, last_operation)
            break
    for index in range(start, end):
        if done == True:
            return equasion
        elif equasion[index] == "+":
            #prnt(equasion, start, end, index)
            equasion[index-1:index+2] = [float(equasion[index-1]) + float(equasion[index+1])]
            fix(equasion, start, end, last_operation)
            break
        elif equasion[index] == "-":
            #prnt(equasion, start, end, index)
            equasion[index-1:index+2] = [float(equasion[index-1]) - float(equasion[index+1])]
            fix(equasion, start, end, last_operation)
            break
        elif str(equasion[index]).lstrip('-').replace(".", "", 1).isdigit():
            continue
        else:
            raise ValueError(f"neplatny priklad {equasion}")
        
def fix(equasion, start, end, last_operation):
    global done
    if int(start) < int(end)-3:
        end -= 2
        calculating(equasion, start, end, last_operation)
    elif last_operation==False:
        evaluating(equasion)
    else:
        print("end")
        done = True

def prnt(equasion, start, end, index):
    print(equasion[start:end])
    print(index)
    print(equasion[index-1], equasion[index], equasion[index+1])

def evaluating(equasion):
    len_equ = len(equasion)
    lenght = 0
    for x in equasion:
        print(x)
        lenght += 1
        if x == ")":
            last_operation = False
            end = equasion.index(x)
            for y in range(1,end+1):
                print(y)
                if equasion[end - y] == "(":
                    start = end-y
                    equasion.pop(start)
                    equasion.pop(end-1)
                    break
            break
        elif lenght == len_equ:
            last_operation = True
            print(equasion, last_operation)
    if last_operation == False:
        calculating(equasion, start, end-1, last_operation)
    else:  
        calculating(equasion, 0, len(equasion), last_operation)

priklad=input("priklad:")
print(listisizing(priklad))