graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3],
}

def stack_dfs(start_v):
    discovered = []
    stack = [start_v]
    
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            print('discovered', discovered)
            stack.extend(graph[v])
            # for i in graph[v]:
            #     stack.append(i)
            print('stack',stack)
    return discovered

print(stack_dfs(1))