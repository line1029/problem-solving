def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))
    cam = routes[0][1]
    num = 1
    for s, e in routes:
        if cam >= s: continue
        cam = e
        num += 1
    return num