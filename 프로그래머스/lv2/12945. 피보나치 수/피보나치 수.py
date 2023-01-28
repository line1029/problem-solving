def solution(n):
    # we can use pisano period, but it's not helpful
    # since range of n of much shorter than mod
    
    # define 2*2 size matrix multiplication
    def matmul22(A, B):
        C = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][j] += A[i][k]*B[k][j]
                C[i][j] %= 1234567
        return C
    
    # identity matrix(for 0th answer) and fibonacci matrix q
    ans = [[1, 0], [0, 1]]
    q = [[1, 1], [1, 0]]
    
    # use binary numeral system to reduce time complexity from O(n) to O(logn)
    while n:
        r = n%2
        if r:
            ans = matmul22(ans, q)
        n //= 2
        q = matmul22(q, q)
    return ans[1][0]

