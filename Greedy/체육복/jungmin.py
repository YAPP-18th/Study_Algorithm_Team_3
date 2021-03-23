def solution(n, losts, reserves):
    reserve = set(reserves) - set(losts) # 진짜 여벌 있는 학생들만 남기기
    lost = set(losts) - set(reserves)
    
    for r in reserve:
        if r-1 in lost: # 잃어버린 사람이면....
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return n - len(lost)