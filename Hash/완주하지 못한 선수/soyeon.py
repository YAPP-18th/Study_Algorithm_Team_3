def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
        
    return participant[len(completion)]

# 효율성 테스트 실패
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
#     for p_name in participant:
#         if p_name not in completion:
#             return p_name
            
#         else:
#             del(completion[completion.index(p_name)])