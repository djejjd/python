"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-10-14
   Author: 张海伦
   Version: 1.0
   Title: 快速排序
"""

import numpy


def SortNum(arr, left_Sort: int, right_Sort: int):
    if arr is None or left_Sort >= right_Sort:
        return
    left = left_Sort
    right = right_Sort
    key = arr[left_Sort]  # 基准点

    # 从数组的两边交替扫描
    while left < right:
        while left < right and key <= arr[right]:
            right = right - 1
        if left < right:
            arr[left] = arr[right]  # 当出现比基准点小的高位进行交换
            left = left + 1
        while left < right and key >= arr[left]:
            left = left + 1
        if left < right:
            arr[right] = arr[left]  # 当出现比基准点大的低位进行交换
            right = right - 1
    arr[left] = key  # 将基准点放回arr[left]中

    SortNum(arr, left_Sort, left-1)
    SortNum(arr, left+1, right_Sort)


if __name__ == '__main__':
    while True:
        num = numpy.random.randint(100, size=20)
        print('排序前的数组: ', num)
        SortNum(num, 0, len(num)-1)
        print('排序后的数组: ', num)
