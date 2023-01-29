def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        cur = f"{arr1[i]|arr2[i]:b}"
        ans.append(" "*(n - len(cur)) + "".join("#" if j=="1" else " " for j in cur))
    return ans