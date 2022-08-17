"""

문제 : 1,1에서 시작해서 여행자가 상하좌우로 이동. 최종 좌표는?

"""
# import sys
#
# n = int(input())
# arr = sys.stdin.readline().rstrip().split(" ")
#
# print(graph, arr)
#
# x=0
# y=0
#
# for i in range(len(arr)) :
#     if arr[i] == "U" :
#         nx = x
#         ny = y-1
#     elif arr[i] == "D":
#         nx = x
#         ny = y+1
#     elif arr[i] == "L" :
#         nx = x-1
#         ny = y
#     elif arr[i] == "R" :
#         nx = x+1
#         ny = y
#     if nx < 0 or nx > 4 or ny < 0 or ny > 4:
#         continue
#
#     x = nx
#     y = ny
#
# print(y+1, x+1)
#
# -------------------------------------------

import sys

n = int(input())
arr = sys.stdin.readline().rstrip().split(" ")

# def solution(dirs):
d = {'U': (-1,0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
x, y = 1, 1
for i in arr:
    ny = y + d[i][0]
    nx = x + d[i][1]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(y, x)