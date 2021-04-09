def solution(numbers, target):
    answer = calculate(numbers, target, 0, 0)
    return answer

def calculate(numbers, target, ret, idx):
    if idx == len(numbers) :
        if ret == target:
            return 1
        return 0

    return calculate(numbers, target, ret + numbers[idx], idx + 1) + calculate(numbers, target, ret - numbers[idx], idx + 1)
    
    