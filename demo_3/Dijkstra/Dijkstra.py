# 单源最短路径
import numpy as np
MAX = 9999999


def dijkstra(v: int, a, dist, prev):
    n = len(dist) - 1
    if v < 1 or v > n:
        return
    s = num = np.array([2] * (n+1), dtype=int)
    for i in range(1, n+1):
        dist[i] = a[v][i]
        s[i] = 0  # 0 == false
        if dist[i] == MAX:
            prev[i] = 0
        else:
            prev[i] = v

    dist[v] = 0
    s[v] = 1  # 1 == true
    for i in range(1, n):
        temp = MAX
        u = v
        for j in range(1, n+1):
            if s[j] == 0 and dist[j] < temp:
                u = j
                temp = dist[j]
        s[u] = 1
        for j in range(1, n+1):
            if s[j] == 0 and a[u][j] < MAX:
                newdist = dist[u] + a[u][j]
                if newdist < dist[j]:
                    dist[j] = newdist
                    prev[j] = u


def traceback(prev, n):
    if n == 1:
        print(n, end=" ")
        return
    traceback(prev, prev[n])
    print(n, end=" ")


if __name__ == '__main__':
    a_list = [[MAX, MAX, MAX, MAX, MAX, MAX], [MAX, 0, 10, MAX, 30, 100],
         [MAX, MAX, 0, 50, MAX, MAX], [MAX, MAX, MAX, 0, MAX, 10],
         [MAX, MAX, MAX, 20, 0, 60], [MAX, MAX, MAX, MAX, MAX, 0]]
    length = len(a_list)
    dist_list = np.array([0] * length, dtype=int)
    prev_list = np.array([0] * length, dtype=int)
    dijkstra(1, a_list, dist_list, prev_list)
    print('顶点1到顶点5的最短距离: ')
    traceback(prev_list, 5)
    print("\n顶点1到3的最短距离: ")
    traceback(prev_list, 3)



