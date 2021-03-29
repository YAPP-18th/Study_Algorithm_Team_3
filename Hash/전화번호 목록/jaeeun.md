```python
# find 로 찾으려했지만 테스트케이스 통과 x & 효율성 3,4번 통과 x
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if not phone_book[j].find(phone_book[i]):
                return False
    return answer
```

```python
# 테스트케이스 13번 통과 못한다.
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
    return answer
```

```python
# zip, startswith 함수로 풀었다. 나중에 시작하는 문자를 풀 때 사용해보도록 한다. 
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            answer = False
            break
    return answer
```

