```python
def solution(people, limit):
    people.sort()
    count, start, end = 0, 0, len(people)-1
    while start < end:
        if people[start] + people[end] <= limit:
            start +=1 
            end -=1
            count +=1
        else:
            end -=1
    return len(people) - count
```

