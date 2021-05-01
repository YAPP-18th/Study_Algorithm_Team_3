import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
WV = [list(map(int, input().split())) for _ in range(N)]

weights = [ele[0] for ele in WV]
values = [ele[1] for ele in WV]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = weights[i-1]
        v = values[i-1]
        
        
        # 가질 수 있는 무게 > 물건 무게
        # 이전 값을 최댓값
        if(j < w):
            dp[i][j] = dp[i-1][j]
        # 가질 수 있는 무게 <= 물건 무게
        # 이전에 구했던 무게와 비교하여 더 큰 값 선택
        else:
            dp[i][j] = max(v + dp[i-1][j - w], dp[i-1][j])
print(dp[N][K])