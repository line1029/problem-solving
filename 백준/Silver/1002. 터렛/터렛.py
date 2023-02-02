from sys import stdin, stdout
stdin.readline()
coor = stdin.read().splitlines()
def get_possible_position(s):
    x1, y1, r1, x2, y2, r2 = map(int, s.split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return "-1"
        return "0"
    r3 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    triangle = [r1, r2, r3]
    triangle.sort()
    if triangle[0] + triangle[1] == triangle[2]:
        return "1"
    elif triangle[0] + triangle[1] < triangle[2]:
        return "0"
    return "2"


stdout.write("\n".join(get_possible_position(s) for s in coor))