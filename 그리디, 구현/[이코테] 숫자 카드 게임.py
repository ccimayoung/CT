#N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    mindata = min(data)
    result = max(result, mindata)

print(result)