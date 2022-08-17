
from itertools import combinations

numbers = [4, 1, 2, 1]
target = 4

numbers2 = [-1]*len(numbers)

arr = numbers+numbers2


result = list(combinations(arr, len(numbers)))
result2 = set()

for i in range(len(result)-1):
    if sum(result[i]) == target :
        result2.add(result[i])

print(result)

