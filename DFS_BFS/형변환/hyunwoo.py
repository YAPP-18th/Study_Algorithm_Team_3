import collections

arrived = []

def solution(begin, target, words):
    global arrived
    arrived = [False for _ in range(len(words))]
    
    answer = dfs(begin, target, words, 0)
    if answer == 100:
        return 0
    
    return answer

def dfs(prev, target, words, cnt):
    global arrived
    
    ret = 100
    
    if prev == target:
        return cnt
    
    for nextIdx, word in enumerate(words):
        if compare(prev, word) and not arrived[nextIdx]:
            arrived[nextIdx] = True
            ret = min(ret, dfs(words[nextIdx], target, words, cnt + 1))
            arrived[nextIdx] = False
            
    return ret

def compare(word1, word2):
    diff = list(filter(lambda idx: list(word1)[idx] != list(word2)[idx] , range(len(word1))))
    if len(diff) == 1:
        return True
    return False
    