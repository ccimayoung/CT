
# def numJewelsInStones(self, J: str, S: str) -> int:
#     freqs = {}
#     count = 0
#
#     #돌의 빈도 수 계산
#
#     for char in S:
#         if char not in freqs :
#             freqs[char] = 1
#         else :
#             freqs[char] += 1
#
#
#     #보석의 빈도 수 합산
#     for char in J :
#         if char in freqs :
#           count += freqs[char]
#
#     return count

# ----------------------------------------------

#
# import collections
#
# def numJewelsInStones(self, J: str, S: str) -> int:
#     freqs = collections.Counter(S)
#     count = 0
#
#     #비교 없이 보석의 빈도 수 합산
#     for char in J :
#         count += freqs[char]
#
#     return count

# ----------------------------------------------

def numJewelsInStones(self, J: str, S: str) -> int:
    return sum(s in J for s in S)