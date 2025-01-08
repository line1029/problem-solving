from datetime import datetime, timedelta
def solution(h1, m1, s1, h2, m2, s2):
    # 0초 기준으로 생각해야 함
    # 1분마다 기본 2번씩 만남, 예외는 정각과 0, 12시
    # 하루 1439분 -> 1439 * 2
    # 정각에 분침 안만남 -> -24
    # 0, 12시에 시침 안만남 -> -2
    # 1439 * 2 - 24 - 2 = 2852
    today = datetime.now()
    start = today.replace(hour=h1, minute=m1, second=s1)
    end = today.replace(hour=h2, minute=m2, second=s2)
    
    res = 0
    if not m1 and not s1:
        res += 1
    # 시침의 위치 : h1 * 5 + m1 / 12
    real_h1, real_h2 = (h1 % 12) * 5 + m1 / 12 + s1 / 720, (h2 % 12) * 5 + m2 / 12 + s2 / 720
    
    if h1 == h2 and m1 == m2:
        if m1 and m1 >= s1 and s2 > m1:
            res += 1
        if s1 and real_h1 >= s1 and s2 > real_h1:
            res += 1
        return res
    elif s1:
        if m1 >= s1:
            res += 1
        if real_h1 >= s1:
            res += 1
            
        now = start.replace(second=0) + timedelta(minutes=1)
        h1, m1, s1 = now.hour, now.minute, now.second
        if not m1 and not s1 and not h1 % 12:
            res -= 1
    else:
        now = start
    diff = int((end - now).total_seconds() // 60)
    res += diff * 2
    for i in range(24):
        clock = now.replace(hour=i, minute=0, second=0)
        if now < clock <= end and not i % 12:
            res -= 1
        if now <= clock < end:
            res -= 1
            if not i % 12:
                res -= 1
    if s2:
        if m2 and m2 < s2:
            res += 1
        if real_h2 and real_h2 < s2:
            res += 1
    return res
