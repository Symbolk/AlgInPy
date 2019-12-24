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
        print("circle")


graph_dict = {
    'a': 'bf',  # 表示 a 指向 b 和 f
    'b': 'cdf',
    'c': 'd',
    'd': 'ef',
    'e': 'f',
    'f': ''
}

print(topo_sort(graph_dict))


def topo_sort2(v, e):
    res = []
    while True:
        nodes = indegree(v, e)
        if nodes == None:
            break
        if nodes == -1:
            print("circle")
            return None
        res.extend(nodes)
    return res


def indegree(v, e):
    if len(v) == 0:
        return None
    # deep clone
    v_tmp = v[:]
    e_tmp = e[:]

    # find nodes whose indegree is 0
    for x in e:
        if x[1] in v_tmp:
            v_tmp.remove(x[1])
    if len(v_tmp) == 0:
        return -1

    for i in v_tmp:
        for _, x in enumerate(e_tmp):
            if i in x:
                e.remove(x)
    for i in v_tmp:
        v.remove(i)

    return v_tmp


v = ['a', 'b', 'c', 'd', 'e', 'f']
e = [('a', 'b'),
     ('a', 'f'),
     ('b', 'c'),
     ('b', 'd'),
     ('b', 'f'),
     ('c', 'd'),
     ('d', 'e'),
     ('d', 'f'),
     ('e', 'f')]
print(topo_sort2(v, e))
