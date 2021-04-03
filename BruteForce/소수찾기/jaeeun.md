```python
def solution(numbers):
  answer = 0
  allnum = list
  for n in rnage (len(numbers)):
    tmp = list(permutations(numbers, n+1))
    allnum += [int(''.join(i)) for i in tmp]
  for n in set(allnum):
    tmp = 0
    for i in range (1, n+1):
      if n % i == 0 n !=0:
        tmp +=1
       if tmp >= 3:
        break
     if tmp == 2:
      	answer += 1
    return answer
```

