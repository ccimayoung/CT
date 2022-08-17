
import math
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    import math

    # 작업 소요 일수를 구한다. 나눠서 올림 처리
    day = []
    for i in range(len(progresses)) :
        day.append(math.ceil((100-progresses[i])/speeds[i]))

    # first는 가장 오래 걸린 소요 일수로 초기에는 0으로 저장해둔다
    answer = []
    first = 0

    #작업일수 길이만큼 for문을 돌린다. 특정작업일수가 초기작업일수보다 크면 새로운 first로 저장한다.
    for k in range(len(day)):
        if day[k] > day[first] :
            answer.append(k-first)
            first = k

    #반복문 이후 남은 작업 내보내기
    answer.append(len(day)-first)

    return answer

