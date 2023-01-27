blks_lst = []


while True:
    data = list(map(int, input().split()))
    if data != [0]:
        blks_lst.append(data)
    else:
        break

def max_rtg(htg):
    if len(htg) == 0:
        return 0
    elif len(htg) == 1:
        return htg[0]
    elif len(htg) == 2:
        return max(min(htg[0], htg[1]) * 2, htg[0], htg[1])
    else:
        mid = len(htg) // 2
        return max(max_rtg(htg[:mid]), max_rtg(htg[mid:]), max_rtg_mid(htg))
    
def max_rtg_mid(htg):
    mid = len(htg) // 2
    index_l = mid - 2
    index_r = mid + 1
    w = 2
    
    if htg[mid] <= htg[mid - 1]:
        h = htg[mid]
        rtg = w * h
    else:
        h = htg[mid - 1]
        rtg = w * h

    while index_l >= 0 and index_r <= len(htg) - 1:
        w = w + 1
        if htg[index_l] <= htg[index_r]:
            h = min(h, htg[index_r])
            rtg = max(rtg, w * h)
            index_r += 1
        else:
            h = min(h, htg[index_l])
            rtg = max(rtg, w * h)
            index_l -= 1

    if index_l < 0:
        while index_r <= len(htg) - 1:
            w = w + 1
            h = min(h, htg[index_r])
            rtg = max(rtg, w * h)
            index_r += 1
    else:
        while index_l >= 0:
            w = w + 1
            h = min(h, htg[index_l])
            rtg = max(rtg, w * h)
            index_l -= 1

    return rtg
    

    

for blks in blks_lst:
    print(max_rtg(blks[1:]))
    
