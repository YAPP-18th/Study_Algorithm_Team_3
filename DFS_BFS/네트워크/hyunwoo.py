arrived = []

def solution(n, computers):
    global arrived
    arrived = [False for _ in range(n)]
    answer = 0
    
    for i in range(len(computers)):
        if dfs(i, computers):
            answer += 1
    return answer

def dfs(prev, computers):
    global arrived
    if arrived[prev]:
        return False
    
    arrived[prev] = True
    
    for nxt in range(len(computers[prev])):
        if computers[prev][nxt] == 1:
            dfs(nxt, computers)
        
    return True
    
