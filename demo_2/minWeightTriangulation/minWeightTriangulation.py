"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-10-23
   Author: 张海伦
   Version: 1.0
   Title: 凸多边形最优三角形划分
"""
import math


def getMinWeightTriangulation(n: int, t, s, p):
    for i in range(1, n):
        t[i][i] = 0
    for r in range(2, n + 1):
        for i in range(1, n - r + 2):
            j = i + r - 1
            t[i][j] = t[i + 1][j] + weight(i - 1, i, j, p)
            s[i][j] = i
            for k in range(i + 1, i + r - 1):
                u = t[i][k] + t[k + 1][j] + weight(i - 1, k, j, p)
                if u < t[i][j]:
                    t[i][j] = u
                    s[i][j] = k


# 　获得权值
def weight(i: int, k: int, j: int, p):
    length_i_k = math.pow(math.pow(p[i][0] - p[k][0], 2) + math.pow(p[i][1] - p[k][1], 2), 0.5)
    length_i_j = math.pow(math.pow(p[i][0] - p[j][0], 2) + math.pow(p[i][1] - p[j][1], 2), 0.5)
    length_k_j = math.pow(math.pow(p[k][0] - p[j][0], 2) + math.pow(p[k][1] - p[j][1], 2), 0.5)
    return int(length_i_j + length_i_k + length_k_j)


def traceback(i: int, j: int, s):
    if i != j:
        traceback(i, s[i][j], s)
        traceback(s[i][j] + 1, j, s)
        print("三角剖分顶点: V" + str(i - 1) + ",V" + str(j) + ",V" + str(s[i][j]))


if __name__ == '__main__':
    points = [[1, 1], [1, 2], [4, 3], [7, 1], [1, 3], [3, 3]]
    p_length = len(points)
    num_t = [[0] * p_length for i in range(p_length)]
    num_s = [[0] * p_length for i in range(p_length)]
    getMinWeightTriangulation(p_length - 1, num_t, num_s, points)
    traceback(1, p_length - 1, num_s)
