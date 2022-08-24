# dfs. 스택 활용(선입후출). 재귀적

def dfs(graph, v, visited) :

    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)






#
# from dfs_bfs.prac import dfs_recursive, dfs_stack
#
#
# assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
# assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]
#
#
# graph = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }
#
#
# def dfs_recursive(node, visited):
#     # 방문처리
#     visited.append(node)
#
#     # 인접 노드 방문
#     for adj in graph[node]:
#         if adj not in visited:
#             dfs_recursive(adj, visited)
#
#     return visited
#
#
# def dfs_stack(start):
#     visited = []
#     # 방문할 순서를 담아두는 용도
#     stack = [start]
#
#     # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
#     while stack:
#         # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
#         top = stack.pop()
#         visited.append(top)
#         # 인접 노드를 방문한다.
#         for adj in graph[top]:
#             if adj not in visited:
#                 stack.append(adj)
#
#     return visited