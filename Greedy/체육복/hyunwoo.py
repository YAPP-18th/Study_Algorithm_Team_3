# 체육복
# n : 2 ~ 30
def solution(n, lost, reserve):
  # reserve 근처의 lost에게 옷을 하나씩 빌려줄 수 있다.
  # 1 0 2 1 1 -> 1 1 0 2 1
  # 부분으로 보면서 해결할 수 있을 거 같다.
  # [1, 1], [1, 2], [0, 1], [0, 2], [2, 2], [0, 0] -> set 이라고 생각
  # 두 개의 원소를 가진 셋의 종류는 위 6가지로 나타낼 수 있다.
  # 결과가 달라지는 것은 4번째 셋인 [0, 2]

  # 전체 배열
  students = [1] * n
  for i in lost:
    students[i - 1] -= 1
  for i in reserve:
    students[i - 1] += 1

  # 앞에서부터 학생 배열을 탐색하는데, 2개 원소만 살펴볼 예정
  for i in range(len(students) - 1): 
    picked = set([students[i], students[i + 1]])

    if picked == set([2, 0]):
      students[i], students[i + 1] = 1, 1
  
  answer = list(filter(lambda x: x > 0, students))
  return len(answer)