"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-11-05
   Author: 张海伦
   Version: 1.0
   Title: 装载问题(回溯法)
"""
import numpy as np


class Loading:
    def __init__(self, n, w, c):
        self.n = n  # 集装箱数目
        self.w = w  # 集装箱重量数组
        self.c = c  # 第一艘轮船的载重量
        self.cw = 0  # 当前载重量
        self.bestw = 0  # 当前最优载重量
        self.r = 0  # 剩余集装箱重量
        self.x = []  # 当前解
        self.bestx = []  # 当前最优解
        self.maxLoading()

    def maxLoading(self):
        # 初始化r, x, bestx
        w = self.w
        for k in range(0, len(w)):
            self.r += w[k]
            self.x.append(0)
            self.bestx.append(0)
        self.traceback(1)

    # 进行回溯
    def traceback(self, i):
        # 到达叶子节点
        if i > self.n:
            # 当前载重量大于目前最优载重量时
            if self.cw > self.bestw:
                # 将当前最优载重量更换，同时将当前最优解更换
                self.bestw = self.cw
                for i in range(len(self.x)):
                    self.bestx[i] = self.x[i]
            return

        # 搜索左子树
        self.r -= self.w[i]
        if self.w[i] + self.cw <= self.c:
            self.x[i] = 1
            self.cw += self.w[i]
            self.traceback(i+1)
            self.x[i] = 0
            self.cw -= self.w[i]

        # 如果当前的cw+r的值大于当前最优解会对右子树进行递归
        if self.cw + self.r > self.bestw:
            self.x[i] = 0
            self.traceback(i+1)
        self.r += self.w[i]

# 获取输入
def get_input():
    weight = []
    path = '/home/warren/projects/PycharmProjects/algorithm/demo_4/MaxLoading/input.txt'
    with open(path, 'r') as f:
        for place, content in enumerate(f.readlines()):
            if place == 0:
                number = int(content.strip())
            elif place == 1:
                weight = content.split()
            else:
                a = int(content.split()[0])
                b = int(content.split()[1])
    f.close()
    weight = np.array(weight, dtype=int)
    return number, weight, a, b


if __name__ == '__main__':
    num, weight_list, ship_c_1, ship_c_2 = get_input()
    p = Loading(num, weight_list, ship_c_1)
    for product in range(len(p.bestx)):
        if p.bestx[product] == 1:
            print('将集装箱'+str(product)+'装入第一艘轮船，货物重量：'+str(weight_list[product]))
    sum_weight = 0
    for t in range(1, len(p.bestx)):
        if p.bestx[t] == 0:
            sum_weight += weight_list[t]
            if sum_weight < ship_c_2:
                print('将集装箱' + str(t) + '装入第二艘轮船，货物重量：' + str(weight_list[t]))

# 测试样例
# 3
# 0 20 35 48 34 46
# 70 50

# 3
# 0 10 40 40
# 50 50

