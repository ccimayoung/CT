
"""

문제 : 첫째 줄 정수 N 입력
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력

"""

h = int(input())

count = 0

for hour in range(h+1) :
    for min in range(60) :
        for sec in range(60) :
            if '3' in str(hour) + str(min) + str(sec) :
                count +=1

print(count)

# n = int(input())
#
# count = 0
# for hour in range(0,n+1) :
#     for min in range(60) :
#         for sec in range(60):
#             print(str(hour) + str(min)+str(sec))
# #
# #             if '3' in (str(hour)+str(min)+str(sec)) :
# #                 count +=1
# #
# # print(count)










































