def solution(clothes):
    closet = {}
    for cloth,type in clothes:
        if type in closet:
            closet[type].append(cloth)
        else:
            closet[type] = [cloth]

    candidate_count = 1
    for clothes in closet.values():
        candidate_count *= (len(clothes) + 1)

    answer = candidate_count - 1
    return answer