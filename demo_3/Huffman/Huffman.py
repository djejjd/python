"""
   Copyright: Copyright(c) 2019 张海伦　All rights reserved
   Created on: 2019-10-29
   Author: 张海伦
   Version: 1.0
   Title: 哈夫曼编码
"""
import os
import heapq
from demo_3.Huffman.Node import Node


class HuffmanTree:
    def __init__(self):
        self.char = []  # 储存输入文件中的字符种类
        self.node = None  # 储存最终构建的二叉树
        self.nodes_list = []  # 储存构建的二叉树的各个节点
        self.char_list = {}  # 储存各个字符和其出现的次数
        self.chars_change = {}  # 储存每个字符对应的编码
        self.get_input()

    # 获取输入中各个字符出现的次数
    def get_input(self):
        path = os.getcwd()+'/input.txt'
        with open(path, 'r') as f:
            for text in f.readlines():
                for i in range(len(text.strip())):
                    content = text.strip()
                    if content[i] not in self.char:
                        self.char.append(content[i])
                        self.char_list[content[i]] = 1
                    else:
                        self.char_list[content[i]] += 1
        f.close()
        self.get_Nodes()
        self.nodes_list = self.HuffmanTrees()
        self.node = self.nodes_list[0]
        self.get_optimal_coding(node=self.node, nums="")
        self.output()

    # 构建节点列表
    def get_Nodes(self):
        heap = []
        for i in self.char_list:
            NewNode = Node(i, self.char_list[i])
            heapq.heappush(heap, NewNode)

        return heap

    # 构建Huffman树
    def HuffmanTrees(self):
        nodes_list = self.get_Nodes()
        while len(nodes_list) != 1:
            a = heapq.heappop(nodes_list)
            b = heapq.heappop(nodes_list)
            node = Node()
            node.weight = a.weight + b.weight
            node.leftChild = a
            node.rightChild = b
            a.parent = node
            b.parent = node
            heapq.heappush(nodes_list, node)

        return nodes_list

    # 获得最优前缀编码
    def get_optimal_coding(self, node, nums):
        if node is None:
            return
        self.get_optimal_coding(node.leftChild, nums + '0')
        if node.character is not None:
            self.chars_change[node.character] = nums
            print(str(node.character) + " 的权值为: " + str(node.weight) + ", 编码为: " + nums)
        self.get_optimal_coding(node.rightChild, nums + '1')

    # 将字母换成编码输出
    def output(self):
        coding = ""
        path_input = '/home/warren/projects/PycharmProjects/algorithm/demo_3/Huffman/input.txt'
        path_output = '/home/warren/projects/PycharmProjects/algorithm/demo_3/Huffman/output.txt'
        fp = open(path_output, 'w')
        with open(path_input, 'r') as f:
            for text in f.readlines():
                for i in range(len(text.strip())):
                    coding += str(self.chars_change[text.strip()[i]])
        fp.write(coding)
        f.close()
        fp.close()


h = HuffmanTree()
