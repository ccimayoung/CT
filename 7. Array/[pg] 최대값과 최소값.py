# s = [-1,3,-4,2]


def solution(s):
    arr = list(map(int, s.split()))

    arr.sort()
    #문자열 공백으로 리턴
    return str(arr[0]) + " " + str(arr[-1])