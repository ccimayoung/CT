import time


import sys
start = time.time()
arr = list(map(int,sys.stdin.readline().rstrip()))



answer = arr[0]

for i in range(len(arr)-1) :

    if (answer * arr[i+1]) > (answer + arr[i+1]) :
        answer = answer*arr[i+1]
    else :
        answer = answer+arr[i+1]

print(answer)

end = time.time()
print(end-start)
