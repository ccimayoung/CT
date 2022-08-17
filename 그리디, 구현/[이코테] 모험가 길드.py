import sys
arr = list(map(int,sys.stdin.readline().rstrip()))

result = 0
count = 0

for i in arr :
    count +=1
    if count >= i:
        result +=1
        count = 0

print(count)