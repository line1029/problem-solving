def solution(n, words):
    visited = set()
    visited.add(words[0])
    for i in range(1, len(words)):
        if words[i] in visited or words[i][0] != words[i-1][-1]:
            return [i%n + 1, i//n + 1]
        visited.add(words[i])
    return [0, 0]