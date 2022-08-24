
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))


def miro_bfs(graph):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    for y in range(n): 
        for x in range(m):
            if graph[y][x] == 0:
                continue

            q = deque([(y, x)])

            while q:
                y, x = q.popleft()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or graph[ny][nx] == 0:
                        continue
                    if graph[ny][nx] == 1 :
                        graph[ny][nx] = graph[y][x] + 1
                        q.append((ny, nx))
    return graph[n-1][m-1]

print(miro_bfs(graph))

