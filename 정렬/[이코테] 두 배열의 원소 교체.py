n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

print(A, B)

for change in range(k):
    if A[change] < B[change] :
        A[change], B[change] = B[change], A[change]
    else :
        break


print(A, B)

print(sum(A))

