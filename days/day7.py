from functools import lru_cache
from utils import files

empty = "."
split = "^"
beam = "|"

def count_paths(ls: list, start: tuple):
    n = len(ls)
    m = len(ls[0])
    x,y = start[0], start[1]

    @lru_cache(maxsize=None)
    def dfs(x: int, y: int) -> int:
        ch = ls[x][y]
        if ch not in ("S", beam):
            return 0
        while x < n - 1:
            next = ls[x+1][y]
            x += 1
            if next == empty:
                return 0
            if next == split:
                return dfs(x, y+1) + dfs(x, y-1)
        if x == n - 1 and ls[x][y] == beam :
            return 1
        return 0
    return dfs(x, y)


def solve(ls: list):
    count = 0
    x = 0
    y = ls[0].index("S")
    start = (x,y)
    ys = set([y])
    while (x < len(ls) - 1):
        to_add = []
        to_remove = []
        for y in ys:
            if ls[x+1][y] == empty:
                ls[x+1][y] = beam
            elif ls[x+1][y] == split:
                ls[x+1][y+1] = beam
                ls[x+1][y-1] = beam
                count += 1
                to_add.append(y+1)
                to_add.append(y-1)
                to_remove.append(y)
        x += 1
        for t in to_remove:
            ys.remove(t)
            to_remove = []
        for t in to_add:
            ys.add(t)
            to_add = []

    # for l in ls:
    #     print(l)

    print(f"part 1: {count}")
    print(f"part 2: {count_paths(ls, start)}")

def main():
    day = 7
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)
    solve(test_lines)
    solve(real_lines)


if __name__ == '__main__':
    main()
