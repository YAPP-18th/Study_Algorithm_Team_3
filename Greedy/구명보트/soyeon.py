def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    for one in people:
        answer += 1
        if one + people[-1] <= limit:
            people.pop()
    return answer