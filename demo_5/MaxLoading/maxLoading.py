import os
import heapq
import numpy as np
from demo_5.MaxLoading.Node import Node


class HeapNode(Node):
    def __init__(self, parent, leftChild, uweight, place):
        super().__init__(parent, leftChild)
        self.uweight = uweight
        self.place = place

    def __lt__(self, other):
        return int(self.uweight) > int(other.uweight)


class MaxLoading:
    def __init__(self, c, w):
        self.c = c
        self.w = w
        self.ew = 0  # 扩展节点所对应的载重量
        self.leave_list = [0 for _ in range(len(self.w))]
        self.nodes_list = []
        self.maxLoading()

    def maxLoading(self):
        e = HeapNode(None, None, None, None)
        # 获得剩余重量数组
        for i in range(len(self.w)):
            for j in range(i + 1, len(self.w)):
                self.leave_list[i] += self.w[j]

        i = 0
        while i != len(self.w):
            # 加入活节点
            if self.ew + self.w[i] <= self.c:
                self.addNode(self.ew + self.w[i] + self.leave_list[i], i + 1, e, True)
            self.addNode(self.ew + self.leave_list[i], i + 1, e, False)

            # 获得下一个扩展节点
            e = heapq.heappop(self.nodes_list)
            if i - 1 < 0:
                i = 1
            i = e.place
            self.ew = e.uweight - self.leave_list[i-1]

        bestx = [0 for _ in range(len(self.w))]
        # 获得结果
        for j in range(len(self.w)-1, -1, -1):
            if str(e.left_child) == 'True':
                bestx[j] = 1
            else:
                bestx[j] = 0
            e = e.parent
        # print(bestx)
        # 打印结果
        for t, j in enumerate(bestx):
            if j == 1:
                print('货物' + str(t + 1) + '质量：' + str(self.w[t]) + '装入货轮中')

    def addNode(self, uweight, place, node, child):
        new_heapnode = HeapNode(node, child, uweight, place)
        heapq.heappush(self.nodes_list, new_heapnode)

def get_input():
    path = os.getcwd()+'/input.txt'
    with open(path, 'r') as f:
        for i, text in enumerate(f.readlines()):
            if i == 0:
                num = int(text.strip())
            elif i == 1:
                weights_list = np.array(text.split(), dtype=int)
    return num, weights_list


num_box, weight_list = get_input()
MaxLoading(num_box, weight_list)

# 测试实例
# 50 [10, 40, 40]
# 30 [16, 15, 15]
# 70 [20, 35, 48, 34, 46]
