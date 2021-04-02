import sys
import itertools
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n + 1):
    permute = itertools.combinations(arr, i)
    answer  = list(filter(lambda x : sum(x) == s, permute))
    count += len(answer)

print(count)