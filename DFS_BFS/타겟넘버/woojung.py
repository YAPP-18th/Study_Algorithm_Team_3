global answer
answer = 0
def dfs(value, i, numbers, target): # value=지금까지 더한 값, i=더한 개수, j=그전에 더한거 0/1
    global answer
    if i == len(numbers)-1:
        if value == target:
            answer += 1
            return 
        
    if i < len(numbers)-1:
        dfs(value + numbers[i+1], i+1, numbers, target)
        dfs(value - numbers[i+1], i+1, numbers, target)

def solution(numbers, target):
    
    dfs(numbers[0], 0, numbers, target)
    dfs(-numbers[0], 0, numbers, target)
        
    return answer