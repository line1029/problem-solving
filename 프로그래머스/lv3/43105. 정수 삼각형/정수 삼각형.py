def solution(triangle):
    n = len(triangle)
    for i in range(1, n):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])