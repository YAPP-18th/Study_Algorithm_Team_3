import itertools

def solution(numbers):
    answer = 0

    # 가능한 숫자 조합 구하기
    number_arr = []
    for i in range(1, len(numbers) + 1):
        for el in list(itertools.permutations(numbers, i)):
            number_arr.append(int("".join(el)))
    
    # 에라토스 테네스의 체 이용하기
    max_num = max(number_arr)
    prime = [1 for i in range(max_num + 1)]
    prime[0] = 0
    prime[1] = 0

    for i in range(2, max_num + 1):
        for j in range(i**2, max_num + 1, i):
            prime[j] = 0
    
    # 소수 검사
    for num in set(number_arr):
       if prime[num] == 1:
           answer += 1
    
    return answer


