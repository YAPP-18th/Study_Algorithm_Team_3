```python
def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_get = set(reserve) - set(lost)
    count = len(real_lost)
    for i in real_get:
        if i+1 in real_lost or i-1 in real_lost:
            count -= 1
    if count > 0:
        return n - count
    else:
        return n
```

