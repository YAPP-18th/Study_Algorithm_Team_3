answer = 0
def nextone(word1, word2): # 한개의 알파벳만 다를 경우 True 반환
    cnt = 0
    n = len(word1)
    for i in range(n):
        if word1[i] == word2[i]:
            cnt += 1
    if cnt + 1 == n:
        return True
    return False

def dfs(begin, target, words, visited):
    global answer
    stack = [begin]  # 스택을 활용한 dfs
    while stack:
        x = stack.pop()
        if x == target: # target과 같아졌을 때 answer 리턴
            return answer
        
        for w in range(0, len(words)):
            if nextone(x, words[w]): # 하나만 다를 경우
                if visited[w] != 0: # 이미 방문했던 거면 그냥 넘어감
                    continue
                visited[w] = 1 # 방문 안했던 거면 방문했다고 표시(1)
                # stack에 추가
                stack.append(words[w]) # 스택에 추가
        answer +=1

    
def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    visited = [0] * len(words)
    
    dfs(begin, target, words, visited)