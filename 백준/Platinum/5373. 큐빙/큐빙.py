from sys import stdin
from itertools import islice
SURFACE_INDEX_MAP = {"U":0, "D":1, "F":2, "B":3, "L":4, "R":5}
ORIENTATION_MAP = {1:[[2, 5, 8], [8, 7, 6], [2, 5, 8], [0, 1, 2]],
                   0:[[0, 1, 2], [6, 3, 0], [8, 7, 6], [6, 3, 0]]}
CUBE_ORDER = "wyrogb"
def rotate(cube, surface: str, orientation: str) -> None:
    surface_idx = SURFACE_INDEX_MAP[surface]
    surface = cube[surface_idx]
    side_edge = ORIENTATION_MAP[surface_idx%2]
    side = [(surface_idx + ((i + 1)//2 + 1)*(-1)**(i + surface_idx%2 + 1))%6 for i in range(4)]
    if orientation == "-":
        side = side[::-1]
        side_edge = side_edge[::-1]
        for i in range(3//2):
            for j in range(i, 3 - i - 1):
                tmp = surface[3*i+j]
                surface[3*i+j] = surface[3*j+2-i]
                surface[3*j+2-i] = surface[3*(2-i)+2-j]
                surface[3*(2-i)+2-j] = surface[3*(2-j)+i]
                surface[3*(2-j)+i] = tmp
    else:
        for i in range(3//2):
            for j in range(i, 3 - i - 1):
                tmp = surface[3*i+j]
                surface[3*i+j] = surface[3*(2-j)+i]
                surface[3*(2-j)+i] = surface[3*(2-i)+2-j]
                surface[3*(2-i)+2-j] = surface[3*j+2-i]
                surface[3*j+2-i] = tmp
    tmp = [cube[side[3]][i] for i in side_edge[3]]
    for side_idx, edge_idx in zip(side, side_edge):
        for i in range(3):
            tmp[i], cube[side_idx][edge_idx[i]] = cube[side_idx][edge_idx[i]], tmp[i]


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    cube = [list(i)*9 for i in CUBE_ORDER]
    for oper in stdin.readline().split():
        rotate(cube, *oper)
    print("\n".join("".join(islice(cube[0], i*3, i*3 +3)) for i in range(3)))