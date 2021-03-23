# testcase 4,7,11 fail
def solution(name):
    answer = 0 
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 상하
    for i in name:
        if alpha.index(i) <= 13:
            answer += alpha.index(i)
        else:
            answer += 26 - alpha.index(i)
    # 좌우
    for i in name:
        if i == 'A':
            name = name.replace(i,'0')
        else:
            name = name.replace(i,'1')
    # greedy : 현재 위치에서 1이 가까운 쪽으로. 
    idx = 0
    name = list(name)
    while True:
        name[idx] = '0'
        left_idx, right_idx = idx-1, idx+1
        # 인덱스 삐져나갈 경우 재조정
        if left_idx < 0:
            left_idx = len(name) - 1
        if right_idx > len(name) - 1:
            right_idx = 0
        # 모두 0이면 break 
        if '1' not in name:
            break
        # 오른쪽이 1인 경우
        elif name[right_idx] == '1' and name[left_idx] == '0':
            answer += 1
            idx = right_idx
            print('case1')
        # 왼쪽이 1인 경우
        elif name[right_idx] == '0' and name[left_idx] == '1':
            answer += 1
            idx = left_idx
            print('case2')
        # 둘다 1인 경우
        elif name[right_idx] == '1' and name[left_idx] == '1':
            answer += 1
            idx = right_idx
            print('case3')
        # 둘다 0인 경우
        elif name[right_idx] == '0' and name[left_idx] == '0':
            answer += 1
            idx = right_idx
            print('case4')
    
    return answer