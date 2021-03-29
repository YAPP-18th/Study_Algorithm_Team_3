from collections import Counter

def solution(clothes):
    answer = 1
    
    # 이중리스트 -> 딕셔너리 변환
    clothes = dict(zip(list(map(list,zip(*clothes)))[0],list(map(list,zip(*clothes)))[1])) # key: 실제 옷 , value: 종류
    val = list(clothes.values())
    l = {}

    # value 개수 세기
    for i in val:
        l[i]=val.count(i)
        
    for k in list(l.values()):
        answer *= (k+1)
    return answer-1