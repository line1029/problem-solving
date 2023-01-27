from sys import stdin
n = int(stdin.readline())
meetings = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
meetings.sort(key=lambda x: (x[1], x[0]))
me = iter(meetings)
room_end = next(me)[1]
cnt = 1
for start, end in me:
    if room_end > start:
        continue
    room_end = end
    cnt += 1
print(cnt)