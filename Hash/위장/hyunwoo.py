def solution(clothes):
    clothes_dict = {}
    for value, key in clothes:
        if key in clothes_dict:
            clothes_dict[key] += 1
        else:
            clothes_dict[key] = 1
    clothes_values = list(clothes_dict.values())
    answer = 1
    for value in clothes_values:
        answer *= (value + 1)
        
    return answer - 1