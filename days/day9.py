from collections import defaultdict
import itertools
from utils import files

def line(p1, p2) -> list:
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == y2:
        return [(x1, y1)]
    elif x1 == x2:
        step = 1 if y2 >= y1 else -1
        return [(x1, y) for y in range(y1, y2 + step, step)]
    elif y1 == y2:
        step = 1 if x2 >= x1 else -1
        return [(x, y1) for x in range(x1, x2 + step, step)]
    else:
        return [(x1, y1), (x2, y2)]


def inside(p1, p2, inside_map):
    x1, y1 = p1
    x2, y2 = p2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not inside_map.get((x, y), False):
                return False
    return True


def solve(ls, offset): 
    dists = defaultdict(list)
    border = set()
    reds = []
    real_reds = defaultdict(tuple)

    for l in ls:
        l = "".join(l)
        x_str, y_str = l.split(",")
        x, y = int(x_str), int(y_str)
        key = (x // offset, y // offset)
        real_reds[key] = ((x, y))
        reds.append(key)

    for i in range(len(reds)):
        for p in line(reds[i], reds[(i + 1) % len(reds)]):
            border.add(p)

    xs = [p[0] for p in border]
    ys = [p[1] for p in border]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    start = (min_x - 1, min_y - 1)
    visited = set()
    stack = [start]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        if (x, y) in border:
            continue
        if x < min_x - 1 or x > max_x + 1 or y < min_y - 1 or y > max_y + 1:
            continue
        visited.add((x, y))
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))

    inside_map = {}
    for x in range(min_x, max_x + 2):
        for y in range(min_y, max_y + 2):
            inside_map[(x, y)] = ((x, y) not in visited)

    for (p1, p2) in itertools.combinations(reds, 2):
        if p1 == p2:
            continue
        (x1, y1) = real_reds[p1]
        (x2, y2) = real_reds[p2]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        dists[area].append((p1, p2))

    for a in sorted(dists.keys(), reverse=True):
        for (p1, p2) in dists[a]:
            if inside(p1, p2, inside_map):
                return a

    
def main():
    day = 9
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)
    print(f"done test: {solve(test_lines, 1)}")
    print(f"done real: {solve(real_lines, 200)}")


if __name__ == '__main__':
    main()
