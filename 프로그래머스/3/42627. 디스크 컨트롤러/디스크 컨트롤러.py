def solution(jobs):
    import heapq
    jobs = sorted(([x[1], x[0]] for x in jobs), key=lambda x: (x[1], x[0]))
    n = len(jobs)
    pq = []
    idx = 0
    cur_time = 0
    res = []
    while pq or idx < n:
        if not pq:
            cur_time = sum(jobs[idx])
            res.append(jobs[idx][0])
            idx += 1
        else:
            nex_job = heapq.heappop(pq)
            cur_time += nex_job[0]
            res.append(cur_time - nex_job[1])
        while idx < n and jobs[idx][1] <= cur_time:
            heapq.heappush(pq, jobs[idx])
            idx += 1
    return sum(res) // n
        
    