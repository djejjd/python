# 0-1背包问题


def get_pack(v, w, m: int, bag):
    n = len(v)
    for i in range(1, n):
        for j in range(1, m + 1):
            if j < w[i]:  # 当背包容量小于物品体积时候不装
                bag[i][j] = bag[i - 1][j]
            else:  # 当背包容量足够装入时
                # bag[i-1][j]表示没装入第i件物品时候背包中物品的价值
                # bag[i-1][j-w[i]]表示装入第i件物品前背包中物品价值加上v[i](第i件物品的价值)后的总价值
                bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - w[i]] + v[i])


def traceback(w, bag, i: int, j: int):
    if i == 0:
        return
    # 如果bag[i][j]==bag[i-1][j]时候说明第i件商品并未装入背包
    if bag[i][j] == bag[i - 1][j]:
        traceback(w, bag, i - 1, j)
    # 反之说明第i件商品装入背包中，此时就要递归到bag[i-1][j-w[i]]中接着进行寻找
    else:
        print("w[" + str(i) + "]", end=" ")
        traceback(w, bag, i - 1, j - w[i])


if __name__ == '__main__':
    value = [0, 8, 10, 6, 3, 7, 2]
    weight = [0, 4, 6, 2, 2, 5, 1]
    capacity = 12
    num_bag = [[0] * (capacity + 1) for i in range(len(weight))]
    get_pack(value, weight, capacity, num_bag)
    traceback(weight, num_bag, len(weight) - 1, capacity)
