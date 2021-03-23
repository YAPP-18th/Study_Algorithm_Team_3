from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
  
    queue = deque(people)
    
    while queue:
        if len(queue) >= 2:
            # 무게 큰 놈이 나감
            if queue[0] + queue[-1] > limit:
                queue.pop()
                answer += 1
            else:
                queue.pop()
                queue.popleft()
                answer += 1
        else:
            if queue[0] <= limit:
                queue.pop()
                answer += 1

    return answer