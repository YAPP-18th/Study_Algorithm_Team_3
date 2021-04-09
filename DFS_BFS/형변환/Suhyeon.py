def solution(begin, target, words):
    answer = 0
    words.append(begin)
    graph = {word: [] for word in words}

    for i in range(len(words)):
        for j in range(i, len(words)):
            count = 0
            for k in range(len(begin)):
                if words[i][k] != words[j][k]:
                    count += 1
            if count == 1:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    answer = bfs(begin, target, graph)
    return answer


def bfs(begin, end, graph):
    min_count = 51
    need_visit = [(begin, set())]
    while need_visit:
        node, path = need_visit.pop()
        if node == end:
            min_count = min(min_count, len(path))

        for adj in graph[node]:
            if adj not in path:
                new_path = path.copy()
                new_path.add(adj)
                need_visit.append((adj, new_path))

    if min_count == 51:
        return 0
    else:
        return min_count