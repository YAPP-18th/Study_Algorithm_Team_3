# N<=1500000 / 시간 2초
# O(N)

import sys
input = sys.stdin.readline

N = int(input())

day = N
T, P = [], []
dp = [0]*(N+1)

for i in range(N):
    temp = list(map(int, input().split()))
    T.append(temp[0]) # 일을 한 경우
    P.append(temp[1]) # 일을 안한 경우

# 
for i in range(0, N):
    if T[i] <= N - i:
        # max(i번째까지 번 돈 + i번째 일함, 일 안하고 넘어감)
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
        
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[N])
