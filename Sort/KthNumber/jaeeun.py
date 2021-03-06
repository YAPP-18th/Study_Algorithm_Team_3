def solution(array, commands):
    answer = []
    array_data =[]
    for i in (commands):
        array_data = array[i[0]-1:i[1]]
        array_data.sort()
        answer.append(array_data[i[2]-1])
    return answer
