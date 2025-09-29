import time
import random
import matplotlib.pyplot as plt
import numpy as np

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr):
    keys = [0] * length
    sorted_arr = [0] * length
    for x in arr:
        keys[x] += 1
    for x in range(1, length):
        keys[x] += keys[x-1]
    for x in arr:#otocit operaci
        sorted_arr[keys[x]-1] = x
        keys[x] -= 1
    return sorted_arr

def insert_sort(x):
    for index in range(0, len(x)):
        mov=0
        while x[index + mov] < x[index - 1 + mov]and index - 1 + mov != -1:
            x[index + mov], x[index - 1 + mov] = x[index - 1 + mov],  x[index + mov]
            mov -= 1
    return x

def select_sort(x):
    for index in range(0, len(x)):
        inum = x[index]
        for num in x[index:]:
            if num < inum:
                inum = num
        if index != x.index(inum, index):
            x.insert(index,x.pop(x.index(inum, index)))
    return x

def bouble_sort(random_list):
    position = len(random_list) - 1
    for n in range(0, len(random_list)-1):
        index = 1
        for x in range(0, position):
            if random_list[index] < random_list[index - 1]:
                random_list[index], random_list[index-1] = random_list[index-1], random_list[index]
                position = index - 1
            index += 1
    return random_list

def coctail_sort(random_list):
    position_end = len(random_list) - 1
    position_start = 0
    for n in range(0, len(random_list)):
        sort=False
        for x in range(position_start, position_end):
            index = x + 1
            if random_list[index] < random_list[index - 1]:
                sort=True
                random_list[index], random_list[index-1] = random_list[index-1], random_list[index]
                position_end = index - 1
        for x in range(-position_end, -position_start):
            index = -x
            if random_list[index] < random_list[index - 1]:
                sort=True
                random_list[index], random_list[index-1] = random_list[index-1], random_list[index]
                position_start = index
        if sort == False:
            return random_list
            break

difference = int(input("difference in lenght of tested lists:"))
tests = int(input("amount of tests:"))
tests_per_list = int(input("amount of tests per list:"))

length = 0
lengths_list = []

for n in range(0, tests):
    length += difference
    lengths_list.append(length)
    keys = [0] * length
    sorted_arr = [0] * length
    for x in range(0,tests_per_list):
        arr =  random.choices(range(0, length),k=length)
        print(f"unsorted: {arr}")
        arr2 = arr[:]
        arr3 = arr[:]
        arr4 = arr[:]
        arr5 = arr[:]
        arr6 = arr[:]
        print(f"insert_sort: {insert_sort(arr)}")
        print(f"select_sort: {select_sort(arr2)}")
        print(f"bouble_sort: {bouble_sort(arr3)}")
        print(f"coctail_sort: {coctail_sort(arr4)}")
        print(f"counting_sort: {counting_sort(arr5)}")
        print(f"quick_sort: {quick_sort(arr6)}")
