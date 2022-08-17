
nums = [1,4,3,2]



#1번 방법
# nums.sort(reverse=True)
# sum=0
# pair = []
#
# for n in nums :
#     pair.append(n)
#     if len(pair) == 2:
#         sum += min(pair)
#         pair = []
#
# print(sum)


#2번 방법
nums.sort()
sum = 0

for i, n in enumerate(nums) :
    #짝수 번째 값 합산. 0부터 시작
    if i %2 ==0:
        sum +=n

print(sum)



#3번 방법
# print(sum(sorted(nums)[::2]))
