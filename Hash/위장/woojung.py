def solution(clothes):
    answer = 0
    hash = {}
    for cloth in clothes:
        if cloth[1] in hash:
            hash[cloth[1]] += 1
        else:
            hash[cloth[1]] = 1

    clo_count = list(hash.values())
    before = 0
    for c in clo_count:
        now = c + c * before
        before += now
        answer += now
    
    return answer

'''
<코드 설명>
ex. 1,2,3,4
단순하게 나열 : (1+2+3)+(1*2+1*3+2*3)+(1*2*3)
for문 이용하여 각 항이 추가될 때마다 그 항과 관련된 항들이 더해지도록.
1 + (2 + 2*1) + (3 + 3*(1+(2+2*1)))
이때 추가되는 수를 a라 하고 그전까지의 값을 before라고 하면, 
a + a * before 형태의 식이 더해진다.

'''

'''
수학 공식 이용
(c+1)을 모두 곱한 다음 -1 

a = 1
    for c in clo_count:
        a *= (c+1)
'''