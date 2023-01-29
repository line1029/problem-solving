def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    cnt = 0
    while left <= right:
        if left < right and people[left] + people[right] <= limit :
            left += 1
            right -= 1
        else:
            right -= 1
        cnt += 1
    return cnt