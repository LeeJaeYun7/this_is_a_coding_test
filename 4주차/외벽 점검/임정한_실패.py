def weak_fixed(weak, starting, worker_ability, direction="R"):
    fixed_weak = []
    for point in weak:
        if direction=="R":
            if starting <= point <= starting+worker_ability:
                continue
            if starting <= point+12 <= starting+worker_ability:
                continue
        else:
            if starting >= point >= starting-worker_ability:
                continue
            if starting >= point >= starting-worker_ability+12:
                continue
        fixed_weak.append(point)
    # print(weak, starting, worker_ability, direction, fixed_weak)
    return fixed_weak

def bfs(weak,dist, starting_point, direction="R", worker_num=0):
    if weak == []:
        return worker_num
    if dist == []:
        return 99999
    _weak = weak_fixed(weak, starting_point,dist[0], direction)
    result = 9999
    for point in weak:
        result = min(result, bfs(_weak,dist[1:],point, "R", worker_num+1))
        result = min(result, bfs(_weak,dist[1:],point, "C", worker_num+1))
    return result

def solution(n, weak, dist):
    dist.sort(reverse=True)
    result = 99999
    for point in weak:
        result = min(result, bfs(weak, dist, point, "R",0 ))
        result = min(result, bfs(weak, dist, point, "C",0 ))
    return result