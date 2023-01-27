def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    ans = sum(A[i]*B[i] for i in range(len(A)))
    return ans