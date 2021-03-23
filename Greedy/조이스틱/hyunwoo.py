# 조이스틱
def solution(name):
    # 최소 이동이 핵심
    # 위, 아래로 카운팅
    # 좌, 우는 A가 있는 경우에 한해서만 유의미
    # JAAAKAAAAAABAA

    name = list(name)
    name = list(map(lambda x: min(ord(x) - ord('A'), ord('Z') + 1 - ord(x)), name))

    answer = 0
    idx = 0
    # 최대 20번 좌,우로 이동
    for i in range(20): 
        answer += name[idx]
        name[idx] = 0
        nextIdx =  findNextIdx(name, idx)
        answer += min(abs(nextIdx - idx), len(name) - abs(nextIdx - idx))
        idx = nextIdx

    return answer

def findNextIdx(arr, idx):
  # idx: 현재 Idx
    for i in range(1, (len(arr) + 1) // 2):
        if arr[(idx + i) % len(arr)] != 0:
            return idx + i
        elif arr[(idx - i) % len(arr)] != 0:
            return idx - i
    return idx