# N, M, K을 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())

# 숫자 N개 받기
data = list(map(int, input().split()))

data.sort(reverse=True)

first = data[0]
sec = data[1]

print(first, sec)

if M%K == 0 :
    secnum = int(M/K) -1
else :
    secnum = int(M/K)

firstnum = M-secnum

result = first*firstnum + sec*secnum
print(result)