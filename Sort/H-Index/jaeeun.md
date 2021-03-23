```python
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
```

[알고리즘 level] 문제명 label: 문제유형

1. 문제에서 사용한 자료구조 및 알고리즘
2. 대략적인 코드 설명