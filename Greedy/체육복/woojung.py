def solution(n, lost, reserve):
    for i in range(0,n+1):
        if i in reserve and i in lost: # 여벌 체육복 있는 친구가 도난당했을 때
            reserve.remove(i) # 제외시킴
            lost.remove(i)
    
    answer = n - len(lost)    
    
    for i in lost: # 앞친구한테 먼저 여부 확인
        if i-1 in reserve: # 앞친구한테 있으면
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve: # 뒷친구한테 있으면
            reserve.remove(i+1)
            answer += 1
    return answer