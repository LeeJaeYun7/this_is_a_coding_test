INF = 999999
OPTIMAL = INF
def weak_fixed(n, weak, starting, worker_ability, direction="R"):
    global OPTIMAL
    fixed_weak = []
    for point in weak:
        if starting <= point <= starting+worker_ability:
            continue
        if point < starting <= point+n <= starting+worker_ability:
            continue
        fixed_weak.append(point)
    return fixed_weak

def bfs(n, weak,dist, starting_point, direction="R", worker_num=0):
    global OPTIMAL
    if weak == []:
        OPTIMAL = min(worker_num, OPTIMAL)
        return 
    if dist == []:
        return 
    if len(weak) == 1:
        OPTIMAL = min(worker_num+1, OPTIMAL)
        return
    if worker_num >= OPTIMAL:
        return
    _weak = weak_fixed(n, weak, starting_point,dist[0], direction)
    if _weak == []:
        OPTIMAL = min( worker_num+1, OPTIMAL)
    for point in _weak:
        bfs(n, _weak,dist[1:],point, "R", worker_num+1)

def solution(n, weak, dist):
    global OPTIMAL
    dist.sort(reverse=True)
    for point in weak:
        bfs(n, weak, dist, point, "R",0)
    if OPTIMAL == INF:
        return -1
    return OPTIMAL