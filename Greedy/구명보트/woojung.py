def solution(people, limit): # 최대 2명이라는 조건!!!!!!!
    answer = 0
    people.sort()
    # 맨앞, 맨뒤사람 더해보고 limit보다 작거나 같으면, 태우고 그 다음 쌍
    # limit 보다 크면, 무거운 애만 태우고, 그다음 무거운애 + 가벼운애 체크
    i, j = 0, len(people)-1
    weight = 0
    while i < j:
        weight = people[i] + people[j]
        if weight <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        answer += 1
    if i == j:
        answer += 1
    
    return answer