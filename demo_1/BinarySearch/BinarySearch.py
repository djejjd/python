"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-10-10
   Author: 张海伦
   Version: 1.0
   Title: 二分查找算法
"""
import random


def BinarySearch(a: list, x: int, n: int):
    left = 0
    right = n - 1

    while left <= right:
        mid = int((left + right) / 2)
        if x == a[mid]:
            return mid
        elif x <= a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    while True:
        num = list(range(random.randint(20, 100)))
        print(num)
        input_number = random.randint(1, 24)
        print(input_number)
        length = len(num)
        result = BinarySearch(num, input_number, length)
        if num[result] == input_number:
            print("True")
        else:
            print('False')
            break


