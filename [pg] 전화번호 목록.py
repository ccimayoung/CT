


phone_book = ["12","123","1235","567","88"]


# 처음에 푼 코드로 코드 실행은 되지만 합계가 낮음. 접두어가 될 번호가 앞에만 있다고 생각해서 다시 풀어봄
# 정확성: 62.5 효율성: 4.2 합계: 66.7 / 100.0
def solution(phone_book):
    a = phone_book[0]
    for i, j in range(1, len(phone_book)):
        if phone_book[i].find(a) == 0:
            return False

    return True



# 정렬을 이용해서 풀었는데 정확성에서 한 문제가 틀림.
# 정확성: 79.2 효율성: 16.7 합계: 95.8 / 100.0
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        if phone_book[i] in phone_book[i+1]:
            return False
    return True


# 다른 풀이를 참고해서 해시테이블을 이용해서 풀음
def solution(phone_book):
    answer = True # 추후 false 값이 없다면 true 값이 나오게 설정
    hash_map = {} # 전화번호 목록을 해시테이블에 넣음
    for number in phone_book:
        hash_map[number] = 1 #value 값은 1로 지정
    for number in phone_book: # 접두어가 해시테이블에 있는지 찾기
        first = ""
        for t in number:
            first += t #
            if first in hash_map and first != number: #해시테이블에 해당 번호가 이미 있고, 동일한 값이 아니라면 false
                answer = False
    return answer # 위 상황이 없었다면 초기 true 값 리턴
