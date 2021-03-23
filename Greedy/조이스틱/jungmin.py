from string import ascii_uppercase
    
def solution(name):
    answer, idx = 0, 0
    
    alphabet = list(ascii_uppercase)
    move = []
    
#     # 상하 이동(알파벳 만들기)
    for spelling in name:
        if alphabet.index(spelling) <= 13:
            move.append(alphabet.index(spelling))
        else:
            move.append(alphabet[::-1].index(spelling)+1)
    
    
    # move = [min(ord(spelling)-ord('A'), ord('Z')- ord(spelling)+1) for spelling in name]
    # print(move)
    
    
    while True:
        answer += move[idx]
        move[idx] = 0 # answer에 넣었으면 0으로 체크해줌.
        
        # 모든 값을 다 순회했으면 break
        if sum(move) == 0:
            break
    
        right, left = 1, 1
        
        # 왼쪽 탐색
        while not move[idx - left]:
            left += 1
        # 오른쪽 탐색
        while not move[idx + right]:
            right += 1
        
        # 값이 더 작은 쪽을 answer에 더한다.
        if left >= right:
            idx += right
            answer += right
        else:
            idx -= left
            answer += left
        
    
    return answer