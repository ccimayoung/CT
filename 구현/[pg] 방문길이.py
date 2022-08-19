dirs = "ULURRDLLU"
x = 0
y = 0
arr = []

for i in range(len(dirs)) :
    if dirs[i] == "U" :
        nx = x
        ny = y+1
    elif dirs[i] == "D":
        nx = x
        ny = y-1
    elif dirs[i] == "L" :
        nx = x-1
        ny = y
    elif dirs[i] == "R" :
        nx = x+1
        ny = y
    if nx < -5 or nx > 5 or ny < -5 or ny > 5:
        continue

    arr.append((x, y, nx, ny))
    arr.append((nx, ny, x, y))

    x = nx
    y = ny

answer = len(set(arr)) / 2
print(answer)

# -----------------------------------------------

# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))
#             s.add((nx,ny,x,y))
#             x, y = nx, ny
#     return len(s)//2