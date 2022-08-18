from itertools import combinations

a = []
for i in combinations([1,3,2,3,2], 2):
   a.append(i)

print(a)
a_set = set(a)
print(a_set)