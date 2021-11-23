# 버블정렬
import random

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if not swap:
            break
    return data


for i in range(10):
    data_list = random.sample(range(100), 10)
    result = bubble_sort(data_list)
    print(result)
