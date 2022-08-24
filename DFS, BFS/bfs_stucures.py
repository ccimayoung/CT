# bfs. 큐 활용(선입선출)

from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    while queue :
        # 큐에서 원소 하나를 pop해서 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결됬지만 미방문 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = {
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}

# 각 노드가 방문한 정보
visited = [False]*9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)