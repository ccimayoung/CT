#
# import time
#
# start_time = time.time()

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

icearray= {0:(0, -1), 1:(0, 1), 2:(1, 0), 3:(-1, 0)}

def dfs(y, x) :
    if y<0 or y>=n or x<0 or x>=m or graph[y][x] != 0 :
        return False

    if graph[y][x] == 0 :
        graph[y][x] =1

        for ice in icearray:
            dfs(y+icearray[ice][0], x+icearray[ice][1])
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1

print(result)





# def ice_dfs(graph):
#     dy = [0,0,1,-1]
#     dx = [1,-1,0,0]
#
#     count = 0
#
#     def dfs(y, x) :
#         # 주어진 범위를 벗어나는 경우에는 즉시 종료
#         if y<0 or y>=n or x<0 or x>=m or graph[y][x] != 0 :
#             return
#
#         graph[y][x] = 1
#         for i in range(4) :
#             dfs(y+dy[i], x+dx[i])
#         return
#
#     for y in range(n) :
#         for x in range(m) :
#             node = graph[y][x]
#             if node != 0 :
#                 continue
#
#             count +=1
#             dfs(y,x)
#
#     return count
#
# print(ice_dfs(graph))
#
# end_time = time.time()
# print("time:", end_time - start_time)