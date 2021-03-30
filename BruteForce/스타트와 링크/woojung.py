from itertools import combinations
n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

li = [i+1 for i in range(n)]
combi = list(combinations(li, n//2)) # 반반 두 팀으로 나누는 모든 경우

answer = 1000 # 가능한 최댓값 = 10명*100 - 10명*1

for i in range(0, len(combi)//2):
    t1,t2 = 0,0 
    sub_combi = list(combinations(combi[i],2)) # team1 구성원 둘씩 짝지음
    sub_combi2 = list(combinations(combi[len(combi)-i-1],2)) # team2 구성원 둘씩 짝지음
    for j in sub_combi: # team1의 점수 계산
        t1 += s[j[0]-1][j[1]-1] + s[j[1]-1][j[0]-1]
    for j2 in sub_combi2: # team2의 점수 계산
        t2 += s[j2[0]-1][j2[1]-1] + s[j2[1]-1][j2[0]-1]
    answer = min(answer, abs(t1-t2))

print(answer)