#
# import sys
# start = sys.stdin.readline().rstrip()
#
# graph = []
# for i in range (1, 9) :
#     graph.append([f"a{i}",f"b{i}",f"c{i}",f"d{i}",f"e{i}",f"f{i}",f"g{i}",f"h{i}"])
# print(graph, start)
#
# newlist=[(i,j) for i in range(len(graph)) for j in range(len(graph[0])) if graph[i][j]==str(start)]
#
# arr = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8']
# d = {'T1': (1,-2), 'T2': (1, 2), 'T3': (-1, -2), 'T4': (-1, 2),
#      'T5': (2,1), 'T6': (2, -1), 'T7': (-2, 1), 'T8': (-2, -1)}
#
# count = 0
#
# for i in arr:
#     x, y = newlist[0][0], newlist[0][1]
#     ny = y + d[i][0]
#     nx = x + d[i][1]
#     if nx < 0 or nx > 7 or ny < 0 or ny > 7:
#         continue
#     count +=1
# print(count)
#
# # -------------------------------------------------------------------


import sys
input = list(sys.stdin.readline().rstrip())

start = [ord(input[0])-96, int(input[1])]

go= {"T1" :(-2, -1), "T2":(-1, -2), "T3":(1, -2), "T4":(2, -1), "T5":(2,1), "T6":(1,2), "T7":(-1,2), "T8":(-2,1)}

gocount = 0
for i in go :
    x= start[1]
    y = start[0]
    nx = x+go[i][1]
    ny= y+go[i][0]
    if(nx>8 or nx<1 or ny>8 or ny<1) :
        continue
    gocount +=1

result = gocount
print(result)


