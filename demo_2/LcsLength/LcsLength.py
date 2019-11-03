# 最长公共子序列

def LcsLength(str_a, str_b, c):
    a = len(str_a) - 1
    b = len(str_b) - 1
    new_str = [[0]*(a+1) for i in range(len(str_b))]
    for i in range(1, a+1):
        new_str[i][0] = 0
    for i in range(1, b+1):
        new_str[0][i] = 0

    for i in range(1, a+1):
        for j in range(1, b+1):
            if str_a[i] == str_b[j]:
                new_str[i][j] = new_str[i-1][j-1] + 1
                c[i][j] = 1
            elif new_str[i-1][j] >= new_str[i][j-1]:
                new_str[i][j] = new_str[i-1][j]
                c[i][j] = 2
            else:
                new_str[i][j] = new_str[i][j-1]
                c[i][j] = 3

    return c[a][b]


def lcs(i, j, a, c):
    if i != 0 and j != 0:
        if c[i][j] == 1:
            lcs(i-1, j-1, a, c)
            print(a[i], end="")
        elif c[i][j] == 2:
            lcs(i-1, j, a, c)
        else:
            lcs(i, j-1, a, c)


if __name__ == '__main__':
    x = ['0', '3', '5', '5', '7', '7', '8', '2', '5', '7']
    y = ['0', '2', '3', '6', '4', '8', '5', '9', '7', '6']
    m = [[0]*len(x) for i in range(len(y))]
    LcsLength(x, y, m)
    lcs(len(x)-1, len(y)-1, x, m)

