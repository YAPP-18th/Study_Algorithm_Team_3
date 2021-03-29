```python
def solution(clothes):
    answer = 1
    closet = dict()
    num_category = []
    
    for name, category in clothes:
        if category in closet:
            closet[category].append(name)
        else:
            closet[category] = [name]
    print(closet)
    for num in closet.keys():
        num_category.append(len(closet[num]))
    
    for i in num_category:
        answer *= (i+1)
        
    return answer -1
```

