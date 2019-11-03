# 矩阵连乘

def MatrixChain(p, m, s):
    n = len(p) - 1
    for i in range(1, n):
        m[i][i] = 0

    for r in range(2, n+1):
        for i in range(1, n-r+2):
            j = i + r - 1
            # 计算当k=i时m[i][j]的初始值
            m[i][j] = m[i+1][j] + p[i-1]*p[i]*p[j]
            # 记录断开位置
            s[i][j] = i
            for k in range(i+1, j):
                # 计算整个取值范围内最小的m[i][j]
                t = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


def traceback(s, i, j):
    if i == j:
        print("A"+str(i), end='')
    else:
        print("(", end='')
        traceback(s, i, s[i][j])
        traceback(s, s[i][j] + 1, j)
        print(")", end='')


if __name__ == '__main__':
    num_p = [30, 35, 15, 5, 10, 20, 25]
    length = len(num_p)
    num_m = [[0]*length for i in range(length)]
    num_s = [[0]*length for i in range(length)]
    MatrixChain(num_p, num_m, num_s)
    traceback(num_s, 1, length - 1)

