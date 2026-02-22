n = int(input())
m = int(input())
raw_edges = eval(input())
durations = eval(input())


adj = {i: [] for i in range(n)}
rev_adj = {i: [] for i in range(n)}
in_degree = [0] * n

for u, v, flag in raw_edges:
    if flag != 'F':
        adj[v].append(u)
        rev_adj[u].append(v)
        in_degree[u] += 1


es = [0] * n
queue = [i for i in range(n) if in_degree[i] == 0]
topo_order = []

while queue:
    u = queue.pop(0)
    topo_order.append(u)
    for v in adj[u]:
        es[v] = max(es[v], es[u] + durations[u])
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

total_time = max(es[i] + durations[i] for i in range(n))
print(f"工程最快完成所需的天数为 {total_time}")


ls = [total_time] * n

for u in reversed(topo_order):
    if not adj[u]:
        ls[u] = total_time - durations[u]
    else:
        min_next_start = min([ls[v] for v in adj[u]])
        ls[u] = min_next_start - durations[u]

for i in range(n):
    print(f"任务 {i} 最晚必须开始的时间是 {ls[i] + 1}")
