import sys
import re

def solution(number, k):
    num_list = list(map(int, str(number)))

    before_max_index = 0

    p=re.compile('[0-8]+')
    m=p.search(number)

    if m :
        while k > 0:
            maxindex=0
            max_num = -1
            delcount = 0
            for i, v in enumerate(num_list):
                if i >= before_max_index and i < before_max_index + k+1:
                    if v==9:
                        max_num = 9
                        maxindex = i
                        break
                    elif v > max_num:
                        max_num = v
                        maxindex = i

            if maxindex > before_max_index :
                for j in range(before_max_index, maxindex):
                    del num_list[j-delcount]
                    k -= 1
                    delcount += 1

            before_max_index = maxindex - delcount +1

            if len(num_list)-before_max_index == k :
                while k>0:
                    num_list.pop()
                    k-=1

            if k == 0:
                break

    else:
        while k > 0:
            num_list.pop()
            k -= 1


    answer = ''.join(str(_) for _ in num_list)

    return answer

print(solution("99999999", 3))