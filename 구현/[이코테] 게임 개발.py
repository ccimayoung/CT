n, m = map(int, input().split())
start_y, start_x, see =map(int, input().split())

graph = []
for i in range(m) :
    graph.append(list(map(int, input().split())))

seewayarray = {0:(-1, 0), 1:(0, -1), 2:(1, 0), 3:(0,1)}
if see == 0:
    i = 1
elif see ==1:
    i =0
elif see == 2:
    i=3
else :
    i=2


visit =[[start_y, start_x]]
cannotgocount = 0
go = True

while go :
        nx = start_x+seewayarray[i][1]
        ny = start_y+seewayarray[i][0]
        goto = [ny, nx]
        print('실행')

        if (goto in visit) or (graph[ny][nx] ==1) :
            if i <3 :
                i+=1
            else :
                i=0
            cannotgocount +=1
            print([ny, nx], '갈수없는곳')

        else :
            visit.append([ny, nx])
            cannotgocount=0
            print([ny, nx], '추가')
            start_y = ny
            start_x=nx
            if i <3 :
                i+=1
            else :
                i=0

        if cannotgocount >=4 :
            print([ny, nx], '못가는거 4번째')
            if i > 0:
                i -= 1
            else:
                i = 3
            nx = start_x - seewayarray[i][1]
            ny = start_y - seewayarray[i][0]


            if graph[ny][nx] ==1 :
                print([ny, nx], '마지막 바다')
                go = False
                break

            else :
                start_y = ny
                start_x = nx
                if i < 3:
                    i += 1
                else:
                    i = 0
                cannotgocount = 0
                print([ny, nx], '뒤돌았음')

result =len(visit)
print(visit, result)


