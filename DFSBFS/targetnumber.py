def make_graph(numbers, target):
    n = len(numbers) + 1
    graph = [[] for _ in range(n)]
    graph[0].append(target)
    for i in range(n):
        for node in graph[i]:
            if i == (n-1):
                break
            graph[i+1].append(node + numbers[n -2 -i])
            graph[i+1].append(node - numbers[n -2 -i])
    return graph

def solution(numbers, target):
    graph = make_graph(numbers, target)
    count = graph[-1].count(0)
    return count