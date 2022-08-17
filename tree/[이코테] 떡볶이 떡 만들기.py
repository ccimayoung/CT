
"""
떡집의 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H 보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.

예를 들어 높이가 19, 14, 10, 17cm 인 떡을 절단기 높이를 15cm로
자르면 떡의 높이는 15, 14, 10, 15cm 가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm로 손님은 6cm 만큼 가져갈 수 있다.

손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 설정할 수 있는
절단기 높이의 최댓값을 구하는 프로그램은?

"""

import sys
import time
n, m = map(int,sys.stdin.readline().split()) # 떡의 개수와 요청한 길이 받기
arr = list(map(int, sys.stdin.readline().rstrip().split(" "))) # 떡 각각의 높이 받기

# start_time = time.time()
start = 0  # 이진탐색 첫 시작점 0으로 설정
end = max(arr) # 이진탐색 첫 끝점을 떡의 높이가 가장 긴 것으로 설정


while(start <= end): # 이진탐색을 시작점과 끝점이 같을 때까지 while문 실행
    give = 0 # 손님에게 줄 떡 길이 설정
    mid = (start+end) // 2 # 중간점 설정. 떡의 길이는 양의 정수로 실수는 버림.
    for i in arr : # 각각의 떡에 대해 실행
        if i > mid : # 떡의 길이가 중간점보다 길다면? 긴만큼 자르고 give에 합산
            give += (i - mid)

    if give < m:  # 손님에게 줄 떡 길이가 요청한 길이보다 짧으면, 끝점을 중간점 앞으로 가져오기
        end = mid -1
    else :  # 손님에게 줄 떡 길이가 요청한 길이보다 길면, 시작점을 중간점 뒤로 가져가기
        H = mid  # mid+1 되기 전, 최대한 덜 잘랐을 때를 H로 설정
        start = mid +1

print(H)
# end_time = time.time()
# print(f"{end_time-start_time:.20f} sec")


import sys
import time
# n, m = map(int,sys.stdin.readline().split()) # 떡의 개수와 요청한 길이 받기
# arr = list(map(int, sys.stdin.readline().rstrip().split(" "))) # 떡 각각의 높이 받기
#
# def dduk(n, m, arr) :
#     start = 0  # 이진탐색 첫 시작점 0으로 설정
#     end = max(arr) # 이진탐색 첫 끝점을 떡의 높이가 가장 긴 것으로 설정
#
#
#     while(start <= end): # 이진탐색을 시작점과 끝점이 같을 때까지 while문 실행
#         give = 0 # 손님에게 줄 떡 길이 설정
#         mid = (start+end) // 2 # 중간점 설정. 떡의 길이는 양의 정수로 실수는 버림.
#         for i in arr : # 각각의 떡에 대해 실행
#             if i > mid : # 떡의 길이가 중간점보다 길다면? 긴만큼 자르고 give에 합산
#                 give += (i - mid)
#
#         if give < m:  # 손님에게 줄 떡 길이가 요청한 길이보다 짧으면, 끝점을 중간점 앞으로 가져오기
#             end = mid -1
#         else :  # 손님에게 줄 떡 길이가 요청한 길이보다 길면, 시작점을 중간점 뒤로 가져가기
#             H = mid  # mid+1 되기 전, 최대한 덜 잘랐을 때를 H로 설정
#             start = mid +1
#
#     print(H)
#
# start_time = time.time()
#
# for k in range(50) :
#     dduk(30, 50000000, [3,100000000,35456,4894897,456456789,545,48948,6548945,456456,1564856596,56465456,4564564564,12317,6549654,15615,3,100000000,35456,4894897,456456789,545,48948,6548945,456456,1564856596,56465456,4564564564,12317,6549654,15615])
# end_time = time.time()
# print(f"{end_time-start_time:.50f} sec")
#
