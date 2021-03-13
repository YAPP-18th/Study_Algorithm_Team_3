// 조합 함수로 풀었지만 시간초과
from itertools import permutations

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    result = list(map(''.join, permutations(numbers)))
    result = list(map(int, result))
    return str(max(result))

// 가장 유명한 풀이
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer