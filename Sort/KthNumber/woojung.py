def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        i,j,k = commands[i]
        new_array = sorted(array[i-1:j])
        answer.append(new_array[k-1])
    return answer