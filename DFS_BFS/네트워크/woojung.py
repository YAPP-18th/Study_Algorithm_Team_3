'''
BFS Algorithm
1.탐색을 위한 큐, 방문한 노드를 체크해 둘 리스트 생성
2.탐색을 시작할 노드를 큐에 넣기 (탐색 시작 노드의 방문 표시 해두기)
3.큐가 빌 때까지 반복문 수행
  3-1.큐의 앞에서부터 노드를 하나씩 꺼내기
  3-2.꺼낸 노드에 인접한 노드들을 방문하는 반복문 수행
    3-2-1.방문한 노드가 이전에 방문한 적이 없다면 큐에 넣기
    3-2-2.방문한 노드는 체크해두기
'''
# 블로그 정답 코드 참고
def solution(n, computers):
    answer = 0
    bfs = [] # 탐색을 위한 큐
    visited = [0] * n # 방문한 노드 체크
    while 0 in visited:	# visited 리스트의 모든 값에 방문 표시(1)가 되어있을 때까지 반복
        x = visited.index(0) # 방문하지 않은 노드 찾아서 x에
        bfs.append(x) 
        visited[x] = 1 # 방문 표시
        
        while bfs: # 큐에 값이 존재하면 반복문 수행
            node = bfs.pop(0) # 큐 맨 앞에서부터
            for i in range(n): # 꺼낸 노드의 인접노드들 반복문으로 훑기
                if visited[i] == 0 and computers[node][i] == 1: # 인접노드이고, 방문된 적이 없는 경우
                    bfs.append(i) # 큐에 추가
                    visited[i] = 1 # 방문됐음(1)
        answer += 1		# 한 네트워크의 탐색을 마치면 개수 추가 
    return answer
    







'''
# 정답률 53% 코드
def solution(n, computers):
    answer = 0
    clist = [0] * n # link가 있으면 1로

    for i in range(0, n-1):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                clist[i], clist[j] = 1,1
    print(clist)
    # clist에서 1이 연속된거는 하나 취급, 0 하나
    prev = False # prev가 0이면 False. 1이면 True
    for c in range(len(clist)):
        if clist[c] == 0:
            if prev == False:
                answer += 1
            elif prev == True:
                answer += 2
            
        elif clist[c] == 1:
            prev = True
            if c == len(clist)-1:
                answer += 1
    
    return answer
'''