```python
# 문제를 제대로 읽지 않았다. participant은 completion보다 1작다는 것을 알았으면 쉽게 풀었을 것 같다.

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
```

