import random
def sort(input_list):
    mem = []
    
    if len(input_list) > 1:
        left = input_list[0]
        right = input_list[1]
        for x in range(0,(len(left) +len(right))):
            if right == [] or left != [] and left[0] < right[0]:
                mem.append(left.pop(0))
            else:
                mem.append(right.pop(0))
        input_list.append(mem)
        input_list.pop(0)
        input_list.pop(0)
        #print(input_list)
        sort(input_list)
        return sort(input_list)
    else:
        return input_list[0]

def split(input_list):
    list_array = []   
    for x in input_list:
        y = []
        y.append(x)
        list_array.append(y)
    return list_array

def merge_sort(input_list):
    list_array = split(input_list)
    return sort(list_array)

l = int(input("Enter the number of elements in the list: "))
numbers = random. sample(range(0, l), l)

print(numbers, len(numbers))
sorted_list = merge_sort(numbers)
print(sorted_list, len(sorted_list))