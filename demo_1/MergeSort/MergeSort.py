"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-10-13
   Author: 张海伦
   Version: 1.0
   Title: 归并排序
"""
import time
import numpy

# 对数组进行拆分，拆成一个一个独立的数
def sortArr(arr, left: int, right: int):
    if left < right:
        mid = int((left + right) / 2)
        sortArr(arr, left, mid)
        sortArr(arr, mid + 1, right)
        merge(arr, left, mid, right)


# 对一个一个的数进行合并排序
def merge(arr, left: int, mid: int, right: int):
    num = [0 for _ in arr]
    a = left
    temp = left
    b = mid + 1

    while left <= mid and b <= right:
        if arr[left] <= arr[b]:
            num[a] = arr[left]
            a = a + 1
            left = left + 1
        else:
            num[a] = arr[b]
            a = a + 1
            b = b + 1

    # 将多余的添加到数组中
    while left <= mid:
        num[a] = arr[left]
        a = a + 1
        left = left + 1

    while b <= right:
        num[a] = arr[b]
        a = a + 1
        b = b + 1

    while temp <= right:
        arr[temp] = num[temp]
        temp = temp + 1


if __name__ == '__main__':
    while True:
        arr_list = numpy.random.randint(100, size=20)
        print('排序前数组: ', arr_list)
        sortArr(arr_list, 0, len(arr_list) - 1)
        print('排序后的数组: ', arr_list)
        time.sleep(3)
