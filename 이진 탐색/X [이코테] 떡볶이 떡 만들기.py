import sys
n, m = map(int,sys.stdin.readline().split())
array = set(map(int, input().split()))


def binary(array, m, start, end):
    H = 0
    while start <= end:
        give = 0
        mid = (start + end) // 2

        for i in array :
            if i>mid :
                give+=(i-mid)

        if give < m:
            end = mid - 1

        else:
            H = mid
            start = mid + 1

    return H

result = binary(array, m, 0, max(array))
print(result)