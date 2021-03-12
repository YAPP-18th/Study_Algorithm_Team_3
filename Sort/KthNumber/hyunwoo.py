def solution(array, commands):
    def cut(arr):
        start = arr[0]
        end = arr[1]
        idx = arr[2]
        slice_arr = sorted(array[start - 1: end])
        return slice_arr[idx - 1]
    answer = list(map(cut, commands))
    return answer