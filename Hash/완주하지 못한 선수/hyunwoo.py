def solution(participant, completion):
    answer = {}
    for el in participant:
        if el in answer:
            answer[el] += 1
        else:
            answer[el] = 1
    
    for el in completion:
        answer[el] -= 1
        if answer[el] == 0:
            del answer[el]
    
    
    return list(answer.keys())[0]