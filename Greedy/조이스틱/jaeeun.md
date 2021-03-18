```python
# 왼쪽 스틱으로 가야하는 경우는 고려하지 않음!?
def solution(name):
    joy = list(name)
    answer = len(joy) -1
    for i in joy:
        if ord(i) <= 77:
            answer += ord(i) - 65
        else:
            answer += 91 - ord(i)
    return answer
```

```python
# 오른쪽 왼쪽 고민했지만 A일때 모르겠음
def solution(name):
    answer = 0
    z = []
    for i in name:
        z.append(min(ord(i)-ord('A'), ord('Z')-ord(i)+1))
    if 'A' not in name:
        answer = len(name)-1 + sum(z)
    else:
        rightIdx=0
        leftIdx=0
        idx=0
        while z[rightIdx+1] == ord('A'):
            rightIdx += 1
        while z[leftIdx -1] == ord('A'):
            leftIdx += 1
        if rightIdx > leftIdx:
            while idx < len(z):
                answer += z[-idx]
                idx +=1
        else:
            while idx < len(z):
                answer += z[idx]
                idx +=1                
    return answer
```

