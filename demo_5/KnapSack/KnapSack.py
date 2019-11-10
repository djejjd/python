"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-11-09
   Author: 张海伦
   Version: 1.0
   Title: 0-1背包问题(分支界限法)
"""
import os
import heapq
import numpy as np
from demo_5.KnapSack.Node import Node
from demo_5.KnapSack.Compare import Compare


class PackNode(Node):
    def __init__(self, parent, child, weight, value, place, uValue):
        super().__init__(parent, child)
        self.weight = weight  # 该节点处相应的质量
        self.value = value  # 该节点所对应的价值
        self.place = place  # 该节点所处的位置
        self.uValue = uValue  # 该节点的价值上界

    def __lt__(self, other):
        return int(self.uValue) > int(other.uValue)


class KnapSack:
    def __init__(self, c, w, p):
        self.c = c  # 背包容量
        self.w = w  # 物品质量数组
        self.p = p  # 物品价值数组
        self.cw = 0  # 当前物品质量
        self.cp = 0  # 当前物品价值
        self.nodes_list = []  # 节点列表
        self.get_compare()
        self.knapsack()

    # 根据单位价值大小进行重新排序
    def get_compare(self):
        nodes_list = []
        for weight, value in zip(self.w, self.p):
            new_node = Compare(weight, value)
            heapq.heappush(nodes_list, new_node)
        for i in range(len(self.w)):
            node = heapq.heappop(nodes_list)
            self.w[i] = node.weight
            self.p[i] = node.value

    # 获得当前节点对应的价值上界
    def get_up_value(self, i):
        cleft = self.c - self.cw  # 背包剩余的容量
        bound = float(self.cp)  # 存储该节点的价值上界

        while i < len(self.w) and cleft >= self.w[i]:
            bound += self.p[i]
            cleft -= self.w[i]
            i += 1

        # 装满背包剩余空间
        if i < len(self.w):
            bound += cleft * (self.p[i] / self.w[i])
        return bound

    def knapsack(self):
        e = PackNode(None, None, None, None, None, None)
        bestp = 0  # 当前最优值
        i = 0
        up_value = self.get_up_value(i)  # 当前的价值上界

        while i != len(self.w):
            if self.cw + self.w[i] <= self.c:
                if self.cp + self.p[i] > bestp:
                    bestp = self.cp + self.p[i]
                self.addNode(e, True, self.cw+self.w[i], self.cp+self.p[i], i+1, up_value)

            up_value = self.get_up_value(i+1)
            # 如果右子树的价值上界大于当前最大价值，说明右子树中可能有最优解，则对右子树进行检查
            if up_value >= bestp:
                self.addNode(e, False, self.cw, self.cp, i+1, up_value)

            # 获得下一扩展节点
            e = heapq.heappop(self.nodes_list)
            i = e.place
            self.cw = e.weight
            self.cp = e.value
            up_value = e.uValue

        bestx = [0 for _ in range(len(self.w))]
        for j in range(len(self.w)-1, -1, -1):
            if str(e.left_child) == 'True':
                bestx[j] = 1
            else:
                bestx[j] = 0
            e = e.parent

        # 打印结果
        for i, j in enumerate(bestx):
            if j == 1:
                print('将质量为: '+str(self.w[i])+',价值为: '+str(self.p[i])+'的物品装入背包中')

    def addNode(self, parent, child, weight, value, place, uValue):
        new_node = PackNode(parent, child, weight, value, place, uValue)
        heapq.heappush(self.nodes_list, new_node)

# 获取输入
def get_input():
    path = os.getcwd()+'/input.txt'
    with open(path, 'r') as f:
        for i, j in enumerate(f.readlines()):
            if i == 0:
                bag = int(j.strip())
            elif i == 1:
                weight_list = np.array(j.split(), dtype=int)
            elif i == 2:
                value_list = np.array(j.split(), dtype=int)
    f.close()
    return bag, weight_list, value_list


bags, weights_list, values_list = get_input()
KnapSack(bags, weights_list, values_list)
