import time
import random
import matplotlib.pyplot as plt
import numpy as np

def insert_sort(x):
    start=time.process_time()
    for index in range(0, len(x)):
        mov=0
        while x[index + mov] < x[index - 1 + mov]and index - 1 + mov != -1:
            x[index + mov], x[index - 1 + mov] = x[index - 1 + mov],  x[index + mov]
            mov -= 1
    end=time.process_time()
    total_time = end-start
    #print(x)
    print("insert_sort execution time:", total_time, "s")
    return total_time

def select_sort(x):
    start=time.process_time()
    for index in range(0, len(x)):
        inum = x[index]
        for num in x[index:]:
            if num < inum:
                inum = num
        if index != x.index(inum, index):
            x.insert(index,x.pop(x.index(inum, index)))
    end=time.process_time()
    #print(x)
    total_time = end-start
    print("select_sort execution time:", total_time, "s")
    return total_time

def bouble_sort(random_list):
    start=time.process_time()
    position = len(random_list) - 1
    for n in range(0, len(random_list)-1):
        index = 1
        for x in range(0, position):
            if random_list[index] < random_list[index - 1]:
                random_list[index], random_list[index-1] = random_list[index-1], random_list[index]
                position = index - 1
            index += 1
    end=time.process_time()
    #print(random_list)
    total_time = end-start
    print("bouble_sort execution time:", total_time, "s")
    return total_time

def coctail_sort(random_list):
    start=time.process_time()
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
            end=time.process_time()
            total_time = end-start
            print("coctail_sort execution time:", total_time,"s")
            return total_time
            break

insert_sort_times = []
select_sort_times = []
bouble_sort_times = []
coctail_sort_times = []

insert_sort_times_average = []
select_sort_times_average = []
bouble_sort_times_average = []
coctail_sort_times_average = []

difference = int(input("difference in lenght of tested lists:"))
tests = int(input("amount of tests:"))
tests_per_list = int(input("amount of tests per list:"))

length = 0
lengths_list = []

for n in range(0, tests):
    length += difference
    print(length)
    lengths_list.append(length)
    for x in range(0,tests_per_list):
        nums = random.sample(range(0,length),length)
        nums2 = nums[:]
        nums3 = nums[:]
        nums4 = nums[:]
        insert_sort_times.append(insert_sort(nums))
        select_sort_times.append(select_sort(nums2))
        bouble_sort_times.append(bouble_sort(nums3))
        coctail_sort_times.append(coctail_sort(nums4))


    #print(insert_sort_times)
    insert_sort_times_average.append(sum(insert_sort_times)/len(insert_sort_times))
    #print(f"insertsort sort average time: {insert_sort_times_average}s for {len(nums)} numbers with {len(insert_sort_times)} attempts")

    #print(select_sort_times)
    select_sort_times_average.append(sum(select_sort_times)/len(select_sort_times))
    #print(f"select sort average time: {select_sort_times_average}s for {len(nums2)} numbers with {len(select_sort_times)} attempts")
    
    #print(bouble_sort_times)
    bouble_sort_times_average.append(sum(bouble_sort_times)/len(bouble_sort_times))
    #print(f"bouble sort average time: {bouble_sort_times_average}s for {len(nums3)} numbers with {len(bouble_sort_times)} attempts")

    #print(coctail_sort_times)
    coctail_sort_times_average.append(sum(coctail_sort_times)/len(coctail_sort_times))
    #print(f"cockatil sort aberage time: {coctail_sort_times_averages}s for {len(nums4)} numbers with {len(coctail_sort_times)} attempts")

#print(insert_sort_times_average)
#print(select_sort_times_average)
#print(bouble_sort_times_average)
#pritn(coctail_sort_times_average)

x1 = np.array(insert_sort_times_average)
x2 = np.array(select_sort_times_average)
x3 = np.array(bouble_sort_times_average)
x4 = np.array(coctail_sort_times_average)
y1 = np.array(lengths_list)

plt.plot(y1, x1, label="insert_sort", ls='solid')
plt.plot(y1, x2, label="select_sort", ls='dashed')
plt.plot(y1, x3, label="bouble_sort", ls='dotted')
plt.plot(y1, x4, label="coctail_sort", ls='-.')

plt.title("comparisons")
plt.ylabel("time in s")
plt.xlabel("lenght in list")
plt.savefig("graph.png")
#plt.show()