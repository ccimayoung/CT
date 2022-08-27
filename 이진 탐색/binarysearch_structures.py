# 재귀 함수를 이용한 이진 탐색
# def binary(array, target, start, end):
#     if start > end:
#         return None
#
#     mid = (start+end)//2
#
#     if array[mid] == target:
#         return mid
#
#     elif array[mid] > target:
#         return binary(array, target, start, mid-1)
#
#     else :
#         return binary(array, target, mid+1, end)
#
# ----------------------------------------------------

# 반복문으로 구현한 이진 탐색

def binary(array, target, start, end):
    while start <= end:
        mid = (start +end) //2

        if array[mid] == target :
            return mid

        elif array[mid] > target :
            end = mid-1

        else :
            start = mid+1

    return None


# n(원소의 개수)와 target(찾고자 하는 문자열) 입력
n, target = list(map(int, input().split()))
# 전체 원소 입력
array = list(map(int, input().split()))

# 이진 탐색 수행 결과
result = binary(array, target, 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다")
else :
    print(result+1)

