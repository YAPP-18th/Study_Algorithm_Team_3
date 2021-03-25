def solution(part, comp):
    answer = ''
    hash = {}
    for p in part: # hash table 구성: key=이름, value=이름 횟수
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
    for c in comp:
        hash[c] -= 1

    # value가 1인 key값 = answer
    for k in hash:
        if hash[k] == 1:
            return k
        
        
'''
다른 답안
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

<추가설명>
collections: Counter 객체
Counter는 hash형 자료들의 값의 개수를 셀때 사용가능
딕셔너리처럼 {'자료 이름' : '개수'} 형식으로 만들어진다
Counter객체끼리 뺄셈가능
    
'''