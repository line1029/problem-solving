def solution(picks, minerals):
    if sum(picks) > len(minerals)//5 + (len(minerals)%5 != 0):
        while sum(picks) > len(minerals)//5 + (len(minerals)%5 != 0):
            if picks[2]:
                picks[2] -= 1
            elif picks[1]:
                picks[1] -= 1
            elif picks[0]:
                picks[0] -= 1
    else:
        minerals = minerals[:5*sum(picks)]
    minerals = [minerals[i*5:(i + 1)*5] for i in range(len(minerals)//5 + (len(minerals)%5 != 0))]
    minerals = [[i.count("diamond"), i.count("iron"), i.count("stone")] for i in minerals]
    minerals.sort(reverse=True)
    ans = 0
    for dia, iron, stone in minerals:
        if picks[0]:
            picks[0] -= 1
            ans += dia + iron + stone
        elif picks[1]:
            picks[1] -= 1
            ans += 5*dia + iron + stone
        else:
            ans += 25*dia + 5*iron + stone
    return ans
        