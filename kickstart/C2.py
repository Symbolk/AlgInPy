T = int(input().strip())


def topo_sort(graph):
    in_degrees = dict((u, 0) for u in graph)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1
    Q = [u for u in graph if in_degrees[u] == 0]
    res = []
    while Q:
        u = Q.pop()
        res.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                Q.append(v)
    if len(res) == len(in_degrees):
        return res
    else:
        return []


for t in range(T):
    R, C = map(int, input().strip().split())
    parent = {}
    pre = list(input().strip())
    if R == 1:
        print('Case #{}: {}'.format(str(t + 1), ''.join(pre)))
    else:
        for r in range(R - 1):
            cur = list(input().strip())
            for i in range(C):
                if pre[i] not in parent:
                    parent[pre[i]] = set()
                if cur[i] not in parent:
                    parent[cur[i]] = set()
                if pre[i] != cur[i]:
                    parent[pre[i]].add(cur[i])
            pre = cur
    
        res = topo_sort(parent)
        if not res:
            print('Case #{}: {}'.format(str(t + 1), -1))
        else:
            print('Case #{}: {}'.format(str(t + 1), ''.join(res[::-1])))
