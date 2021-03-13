# Timeout
from itertools import permutations

def solution(numbers):
    permute = list(permutations(numbers,len(numbers))) 
    list_permute = [''.join(map(str,i)) for i in permute] 
    
    answer = max(list_permute) 
    return answer

# Best // lambda 이용
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
