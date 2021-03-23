import math

def solution(people, limit):
    # 최대 2명
    # 모든 사람을 구출하기 위한 최소 구명보트 개수
    
    bigger = []
    lighter = []
    for i in people:
        if i > limit / 2 :
            bigger.append(i)
        else :
            lighter.append(i)  
            
    bigger = sorted(bigger)
    lighter = sorted(lighter, reverse=True)
    
    count = 0
    biggerIdx = 0
    lighterIdx = 0
    pickedLighter = 0
    
    # bigger 혹은 lighter 배열을 모두 탐색할 때까지 진행
    while len(bigger) > biggerIdx and len(lighter) > lighterIdx:
        picked = bigger[biggerIdx]
        remainder = limit - picked
        
        # 내림차순으로 정렬된 lighter 배열에서 remainder보다 작은 숫자 선택
        for i in range(lighterIdx, len(lighter)):
            lighterIdx = i
            
            if lighter[i] <= remainder:
                pickedLighter += 1
                lighterIdx = i + 1
                break
                
        biggerIdx += 1
        count += 1
    
    # lighter 배열 탐색 완료한 경우
    count += len(bigger) - biggerIdx

    count += math.ceil((len(lighter) - pickedLighter) / 2)
    return count

    """
    처음엔 pop으로 진행하니 시간초과가 계속 진행되었고, 결국 두 배열에 대해
    idx를 통해 카운트하는 방식으로 코드를 구성했다.

    def solution(people, limit) :
        answer = 0
        people.sort()

        a = 0
        b = len(people) - 1
        while a < b :
            if people[b] + people[a] <= limit :
                a += 1
                answer += 1
            b -= 1
        return len(people) - answer

        head >= tail이 될때까지 head, tail을 더했을 때, limit보다 작으면 
        정답(+ 1)에 추가한다.
        전체 사람 수에서 2인 보트의 경우를 빼주는 것이 핵심인 듯 하다. 

    """