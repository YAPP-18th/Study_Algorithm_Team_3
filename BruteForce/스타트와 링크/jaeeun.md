```python
from itertools import combiations
import sys

N = int(sys.stdin.readline())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
answer = sys.maxsize

members = combinations(range(N), N//2)

for member in members:
  a = set(member)
  b = list(set(range(N)) -a)
  a = list(a)
  start, link = 0, 0
  for i in range (N// 2-1):
    for j in range (i+1 , N //2):
      start += table[a[i]a[j]] + tale[a[j]a[i]]
      linke += table[b[i]b[j]] + table[b[j]b[i]]
   answer = min(answer, ab(start -link))
   print(answer)
```

