def solution(arr, k):
    answer = []
    ans_set = set()
    for num in arr:
        if num not in ans_set:
            ans_set.add(num)
            answer.append(num)
        if len(answer) == k:
            return answer
    answer += [-1] * (k - len(answer))
    return answer