import heapq
import numpy as np
from demo_3.MinTree.Kruskal.EdgeNode import EdgeNode


def Kruskal(num: int, points):
    heap = []
    start_list = []
    for i in range(len(points)):
        heapq.heappush(heap, EdgeNode(points[i][0], points[i][1], points[i][2]))

    min_edge = heapq.heappop(heap)
    # 将第一条边的两个节点加入初始节点中
    start_list.append([min_edge.start, min_edge.finish])

    print('添加边: v' + str(min_edge.start) + ' - v' + str(min_edge.finish) + " 权值为: " + str(min_edge.weight))
    # 循环到最后所有的连通分支被合并为一个
    while len(start_list[0]) != num:
        min_edge = heapq.heappop(heap)
        response = 0
        for point in start_list:
            # 当新pop出的最小边的两个端点属于某个连通分支时，将response赋值为3取消循环
            if min_edge.start in point and min_edge.finish in point:
                response = 3
                break
            # 当新pop出的最小边的一个端点属于某个连通分支时，将response复制为1取消循环
            elif min_edge.start in point:
                point.append(min_edge.finish)
                response = 1
                break
            elif min_edge.finish in point:
                point.append(min_edge.start)
                response = 2
                break
            # 当新pop出的最小边的两个端点不属于所有已知的连通分支时，结束循环,
            else:
                pass
        # 当response=1时说明出现了一个新的连通分支
        if response == 0:
            start_list.append([min_edge.start, min_edge.finish])
        # 当response!=3时说明可能有两个连通分支需要合并，并对新加入的边进行输出打印
        if response != 3:
            for i in range(len(start_list)-1):
                for j in range(i + 1, len(start_list)):
                    if set(start_list[i]) & set(start_list[j]) != set([]):
                        m, n = start_list[i], start_list[j]
                        start_list.pop(i)
                        start_list.pop(j-1)
                        start_list.append(list(set(m) | set(n)))
                        break
            print('添加边: v' + str(min_edge.start) + ' - v' + str(min_edge.finish) + " 权值为: " + str(min_edge.weight))

# 获得输入
def get_input():
    a = []
    path = '/home/warren/projects/PycharmProjects/algorithm/demo_3/MinTree/Kruskal/input.txt'

    with open(path, 'r') as f:
        for read in f.readlines():
            a.append(read.split())
    f.close()

    a = np.array(a, dtype=int)
    return a


if __name__ == '__main__':
    points_list = get_input()
    num_points = 7

    Kruskal(num_points, points_list)

# 测试用例
# 0 1 1
# 0 2 5
# 0 3 6
# 1 2 8
# 1 4 4
# 2 3 7
# 2 4 2
# 3 5 3
# 4 5 9

# 0 1 5
# 0 2 2
# 0 3 5
# 1 4 4
# 2 4 3
# 2 5 9
# 2 6 8
# 3 6 3
# 4 5 5
# 5 6 6