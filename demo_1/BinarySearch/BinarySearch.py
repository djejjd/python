# 二分查找
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
        input_number = 10
        length = len(num)
        result = BinarySearch(num, input_number, length)
        if num[result] == input_number:
            print("True")
        else:
            break


