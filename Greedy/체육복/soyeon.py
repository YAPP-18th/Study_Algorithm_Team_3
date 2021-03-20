def solution(n, lost, reserve):
    count_lost=set(lost)-set(reserve)
    count_reserve=set(reserve)-set(lost)
    
    for i in count_lost:
        if i-1 in count_reserve:
            count_reserve.remove(i-1)
        elif i+1 in count_reserve:
            count_reserve.remove(i+1)
        else:
            n=n-1
    return n


# 테스트 케이스 11 통과 못함
# def solution(n, lost, reserve):
#     answer = []
#     count_lost=list(set(lost)-set(reserve))
#     count_reserve=list(set(reserve)-set(lost))
    
#     for i in count_lost:
#         if (len(count_lost)==0)or(len(count_reserve)==0):
#             break
#         else:
#             if i-1 in count_reserve:
#                 count_reserve.remove(i-1)
#                 count_lost.remove(i)
#             elif i+1 in count_reserve:
#                 count_reserve.remove(i+1)
#                 count_lost.remove(i)
#     answer.append(n-len(count_lost))
                
#     for i in count_lost:
#         if (len(count_lost)==0)or(len(count_reserve)==0):
#             break
#         else:
#             if i+1 in count_reserve:
#                 count_reserve.remove(i+1)
#                 count_lost.remove(i)
#             elif i-1 in count_reserve:
#                 count_reserve.remove(i-1)
#                 count_lost.remove(i)
                
#     answer.append(n-len(count_lost))
#     print(answer)
#     return max(answer)