import sys
import itertools
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
sum = 0

if s == 0:
    count -= 1

def solution(arr, sum, idx):
    if idx == len(arr):
        if sum == s:
            global count
            count += 1 
        return
    solution(arr, sum + arr[idx], idx + 1)
    solution(arr, sum, idx + 1)

solution(arr, sum, 0)
print(count)
