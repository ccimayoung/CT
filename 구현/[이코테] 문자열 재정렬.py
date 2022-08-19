
"""

숫자와 알파벳 대문자가 섞인 문자열을 받아서 알파벳을 순차적으로 내보내고 숫자는 더해서 붙이기.
K1KA5CB7 >> ABCKK13

"""

# import sys
# data = sys.stdin.readline().rstrip()
#
# arr = list(map(int, filter(str.isdigit, data)))
# brr = list(filter(str.isalpha, data))
#
# sum = 0
# for i in arr :
#     sum += i
#
# brr.sort()
#
# print(''.join(brr)+str(sum))

# ----------------------------------------------


import sys
data = sys.stdin.readline().rstrip()

result = []
value = 0

for x in data :
    if x.isalpha():
        result.append(x)
    else :
        value +=int(x)

result.sort()

if value != 0 :
    result.append(str(value))

print(''.join(result))