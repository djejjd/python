"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-11-07
   Author: 张海伦
   Version: 1.0
   Title: 0-1背包(回溯法)
"""
import os
import numpy

from demo_4.Knapsack.Product import Element


class Knapsack:
    def __init__(self, c, n, w, p):
        self.c = c  # 背包容量
        self.n = n  # 物品个数
        self.w = w  # 物品重量数组
        self.p = p  # 物品价值集合
        self.cw = 0  # 背包中物品当前质量总和
        self.cp = 0  # 背包中物品当前价值总和
        self.x = [0 for _ in range(len(self.w))]  # 当前解
        self.bestx = [0 for _ in range(len(self.w))]  # 当前最优解
        self.bestp = 0  # 当前最优价值
        self.knapsack()

    def knapsack(self):
        nodes_list = []
        sorted_nodes_list = [0 for _ in range(len(self.w))]
        num_list = [num for num in range(len(self.w))]
        # 获得根据价值排序后的节点数组
        for weight, value, i in zip(self.w, self.p, num_list):
            new_node = Element(i, weight, value)
            nodes_list.append(new_node)
        nodes_list.sort()
        for i in range(len(nodes_list)):
            n = self.n - 1 - i
            sorted_nodes_list[n] = nodes_list[i]
        self.traceback(0, sorted_nodes_list)
        print('最优价值: '+str(self.bestp)+"\n"+'最优方案: '+str(self.bestx))

    def traceback(self, i, nodes):
        # 到达叶节点
        if i >= self.n:
            self.bestp = self.cp
            for k in range(len(self.x)):
                self.bestx[k] = self.x[k]
            return

        # 对左子树进行回溯

        if self.cw + nodes[i].weight <= self.c:
            self.cw += nodes[i].weight
            self.x[nodes[i].id] = 1
            self.cp += nodes[i].value
            self.traceback(i + 1, nodes)
            self.x[nodes[i].id] = 0
            self.cw -= nodes[i].weight
            self.cp -= nodes[i].value

        # 对右子树进行回溯
        if self.bound(i + 1, nodes) > self.bestp:
            self.x[nodes[i].id] = 0  # 进入右子树
            self.traceback(i + 1, nodes)

    # 获得右子树的上界
    def bound(self, i, nodes):
        cleft = self.c - self.cw  # 背包剩余容量
        bound = float(self.cp)  # 当前背包中的物品价值总量

        while i < self.n and cleft >= nodes[i].weight:
            bound += nodes[i].value
            cleft -= nodes[i].weight
            i = i + 1

        # 装满背包
        if i < self.n:
            bound += cleft * (nodes[i].value / nodes[i].weight)
        return bound


# 获取输入
def get_input():
    path = os.getcwd()+'/input.txt'
    with open(path, 'r') as f:
        for i, content in enumerate(f.readlines()):
            if i == 0:
                bag = int(content.strip())
            elif i == 1:
                num = int(content.strip())
            elif i == 2:
                weight_list = numpy.array(content.split(), dtype=int)
            elif i == 3:
                value_list = numpy.array(content.split(), dtype=int)
    return bag, num, weight_list, value_list


t = Knapsack(get_input()[0], get_input()[1], get_input()[2], get_input()[3])
# 测试实例
# 7, 4, [3, 5, 2, 1], [9, 10, 7, 4]
# 9, 4, [2, 3, 4, 5], [3, 4, 5, 7]
# 12, 5, [1, 3, 2, 6, 2], [2, 5, 3, 10, 4]
