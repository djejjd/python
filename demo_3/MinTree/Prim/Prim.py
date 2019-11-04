# 最小生成树之prim算法
import re
import numpy as np
import sys


def prim(v: int, points):
    n = len(points) - 1
    lowcost = np.array([sys.maxsize] * (n + 1), dtype=int)
    closest = np.array([sys.maxsize] * (n + 1), dtype=int)
    min_point = v
    start = [min_point]

    # 对lowcost, closest进行初始化
    for i in range(n + 1):
        closest[i] = v
        if i == v:
            lowcost[i] = 0
        else:
            lowcost[i] = points[v][i]

    while len(start) < len(points):
        last_point = min_point
        min_point_weight = sys.maxsize
        # 获取最小权值
        for i in range(n + 1):
            if lowcost[i] == 0:
                pass
            elif lowcost[i] < min_point_weight:
                min_point_weight = lowcost[i]
                min_point = i
                k = i
        # 将最小权值的边对应的点加入start中
        print('添加边: v' + str(closest[k]) + '-v' + str(min_point) + ' weight: ' + str(min_point_weight))
        start.append(min_point)
        # 更新lowcost, closest
        for i in range(n + 1):
            if lowcost[i] > points[min_point][i]:
                if i in start:
                    lowcost[i] = 0
                else:
                    lowcost[i] = points[min_point][i]
                    closest[i] = min_point


# 获得输入
def get_input():
    a = []
    path = '/home/warren/projects/PycharmProjects/algorithm/demo_3/MinTree/Prim/input.txt'

    with open(path, 'r') as f:
        for read in f.readlines():
            a.append(read.split())
    f.close()

    a = np.array(a, dtype=int)
    return a


if __name__ == '__main__':
    v_start = 0
    points_list = get_input()
    prim(v_start, points_list)

