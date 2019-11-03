import numpy as np


def greedySelector(s, f, a):
    a[0] = 0
    count = 1  # 记录符合安排的活动的个数
    j = 0

    for i in range(1, len(s)):
        # 此时第i个活动和第j个不冲突
        if s[i] >= f[j]:
            a[i] = 0
            j = i
            count = count + 1
        else:
            a[i] = 1
    return count


def output(a, count):
    print("共" + str(count) + "个活动符合安排")
    for i in range(len(a)):
        if int(a[i]) == 0:
            print(str(i + 1), end=" ")


if __name__ == '__main__':
    num_s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    num_f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    num = np.array([2] * len(num_s), dtype=int)
    times = greedySelector(num_s, num_f, num)
    output(num, times)
# 1 4 8 11
