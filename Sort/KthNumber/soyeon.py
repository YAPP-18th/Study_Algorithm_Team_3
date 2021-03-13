# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수

def solution(array, commands):
    answer=[]
    for sub_command in commands:
        sub_array= array[sub_command[0]-1:sub_command[1]]
        sub_array.sort()
        answer.append(sub_array[sub_command[2]-1])
    return answer

#Better
# def solution(array, commands):
#     answer=[]
#     for sub_command in commands:
#         i, j, k = sub_command
#         sub_array=sorted(array[i-1:j])
#         answer.append(sub_array[k-1])
#     return answer

