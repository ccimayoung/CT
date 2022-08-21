
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
#
# 입력 조건
# 첫째 줄에 하나의 문자열 S가 주어집니다. (1 ≤ S의 길이 ≤ 10,000)
#
# 출력 조건
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
#
# 입력 예시1
# K1KA5CB7
#
# 출력 예시1
# ABCKK13
#
# 입력 예시2
# AJKDLSI412K4JSJ9D
#
# 출력 예시2
# ADDIJJJKKLSS20

import sys
data = list(sys.stdin.readline().rstrip())

str_array = [i for i in data if i.isalpha()]
str_array.sort()

num_array = [int(i) for i in data if i.isnumeric()]
number_sum = 0

for i in num_array :
    number_sum+=i

str_result = "".join(str_array)
print(str_result+str(number_sum))



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


# import sys
# data = sys.stdin.readline().rstrip()
#
# result = []
# value = 0
#
# for x in data :
#     if x.isalpha():
#         result.append(x)
#     else :
#         value +=int(x)
#
# result.sort()
#
# if value != 0 :
#     result.append(str(value))
#
# print(''.join(result))