# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
# m=int(input())
# buylist=list(map(int, input().split()))
#
# def binary(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#
#         elif array[mid] > target:
#             end = mid - 1
#
#         else:
#             start = mid + 1
#
#     return None
#
# for buy in buylist:
#     result = binary(array, buy, 0, n-1)
#     if result != None:
#         print ('yes', end=" ")
#     else :
#         print('no', end=" ")

# set 이용

n = int(input())
array = set(map(int, input().split()))

m=int(input())
buylist=list(map(int, input().split()))

for buy in buylist :
    if buy in array:
            print ('yes', end=" ")
    else :
            print('no', end=" ")

