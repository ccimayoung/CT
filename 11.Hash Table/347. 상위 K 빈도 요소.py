import collections

nums = [1,1,1,2,2,3]
k = 2

# class Solution:
#     def topKFrequent(self, nums, k):

#숫자별 빈도 계산해서 리스트에 담긴 튜플형태로 만들어주기
freqs = collections.Counter(nums).most_common()
print(freqs)
result = []

#빈도가 K 이상일 때 해당 숫자를 result에 넣기
for i, j in freqs:
    if j >= k:
        result.append(i)

print(result)


    # # -------------------------------------
    # #
    # # def topKFrequent(self, nums, k):
    #  return list(zip(*collections.Counter(nums).most_common(k)))[0]
