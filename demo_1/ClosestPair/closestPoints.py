# 最近点对问题求解
import random
import sys


sys.setrecursionlimit(10000)  # set the maximum depth as 10000

point = []
x_point = []
y_point = []
distance_point = []
min_length_x = 999999999


# 输入点坐标
def get_point(x: int, y: int):
    i = (x, y)
    if i in point:
        pass
    else:
        x_point.append(i)
        point.append(i)


# 排序
def sort_point(num: list, left_sort: int, right_sort: int, i: int, j: int):
    left = left_sort
    right = right_sort

    if left > right:
        return
    p = num[left]
    while left < right:
        while num[right][i] > p[i] and left < right:
            right = right - 1
        temp = num[right]
        num[right] = num[left]
        num[left] = temp

        while num[left][i] <= p[i] and left < right:
            left = left + 1
        temp = num[left]
        num[left] = num[right]
        num[right] = temp

    sort_point(num, left_sort, right - 1, i, j)
    sort_point(num, left + 1, right_sort, i, j)


# 求距离
def get_distance(a: int, b: int) -> float:
    length = int((a[0] - b[0])) * int((a[0] - b[0])) + int((a[1] - b[1])) * int((a[1] - b[1]))
    return float('%.2f' % pow(length, 0.5))


# 求点集的最短距离
def get_min_distance(min_length: int, num: list, left_point: int, right_point: int, k: int):
    if k == 0:
        t = num[left_point]
        left = left_point + 1
        right = right_point
        while left <= right:
            length = get_distance(t, num[left])
            if min_length > length != 0:
                min_length = length
            left = left + 1
        if left_point + 1 <= right_point:
            get_min_distance(min_length, num, left_point + 1, right_point, k)
        else:
            distance_point.append(min_length)
    else:
        t = num[left_point]
        left = left_point + 1
        right = right_point
        while k <= 6 and left <= right:
            length = get_distance(t, num[left])
            if min_length > length != 0:
                min_length = length
            left = left + 1
            k = k + 1
        if left_point + 1 <= right_point:
            get_min_distance(min_length, num, left_point + 1, right_point, 1)
        else:
            distance_point.append(min_length)


# 得到在d-L和d+L中的点集,并使用归并排序进行排序求距离
def sort_point_in_d(num: list, left_point: int, right_point: int):
    left = left_point
    right = right_point
    for i in num:
        if left <= i[0] <= right:
            y_point.append(i)
    merge_sort(y_point, 0, len(y_point) - 1, 1)


# 归并排序
def merge_sort(num: list, left_point: int, right_point: int, j: int):
    if left_point >= right_point:
        return
    mid_y = int((left_point + right_point) / 2)

    merge_sort(num, left_point, mid_y, j)
    merge_sort(num, mid_y + 1, right_point, j)
    merge(y_point, left_point, mid_y, right_point, j)


def merge(num: list, left_point: int, mid_: int, right_point: int, j: int):
    left = left_point
    temp = left_point
    b = mid_ + 1
    arr = [(0, 0) for i in range(len(num))]

    while left_point <= mid_ and b <= right_point:
        if num[left_point][j] > num[b][j]:
            arr[left] = num[b]
            b = b + 1
            left = left + 1
        else:
            arr[left] = num[left_point]
            left = left + 1
            left_point = left_point + 1

    while left_point <= mid_:
        arr[left] = num[left_point]
        left = left + 1
        left_point = left_point + 1

    while b <= right_point:
        arr[left] = num[b]
        left = left + 1
        b = b + 1
    while temp <= right_point:
        num[temp] = arr[temp]
        temp = temp + 1


# 暴力法求解最近点对中最近的距离
def get_min_distance_by_violence(minlength: int, num: list, left_point: int, right_point: int):
    if len(num) == 1:
        return minlength
    elif len(num) == 2:
        return get_distance(num[left_point], num[right_point])
    else:
        for i in num:
            for j in num:
                length = get_distance(i, j)
                if minlength > length != 0:
                    minlength = length
    return minlength


if __name__ == '__main__':
    while True:
        for kq in range(10):
            get_point(random.randint(1, 10), random.randint(1, 10))

        minLength_by_violence = get_min_distance_by_violence(min_length_x, point, 0, len(point) - 1)

        # 对点集按照x坐标排序并划分
        sort_point(x_point, 0, len(x_point) - 1, 0, 1)
        mid = int(len(x_point) / 2)

        # 求左右两部分点集的最短距离
        get_min_distance(min_length_x, x_point, 0, mid, 0)
        get_min_distance(min_length_x, x_point, mid + 1, len(x_point) - 1, 0)
        d = min(distance_point)

        # 求出在mid-d和mid+d之间的点集
        sort_point_in_d(x_point, int(mid - d), int(mid + d))
        # 求出mid-d和mid+d点集间的最小距离
        get_min_distance(min_length_x, y_point, 0, len(y_point) - 1, 1)

        if minLength_by_violence == min(distance_point):
            print("True")
        else:
            break

