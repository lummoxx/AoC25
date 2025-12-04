
from collections import defaultdict, deque

walls = defaultdict(lambda:False)
# sys.setrecursionlimit(sys.getrecursionlimit()*10)

def in_bounds(row : int, col : int, lines : list) -> bool:
    return (row < len(lines) and col < len(lines[0]) and row > -1 and col > -1)

def manhattan_distance(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)


def shortest_paths(start, goal, pad):

    x1, y1 = start
    x2, y2 = goal

    directions = { "v":(1,0), "<":(0,-1), ">":(0,1),"^":(-1,0)}

    queue = deque([(x1, y1, [(x1, y1)])])
    visited = defaultdict(list)
    shortest_len = float('inf')
    all_paths = []

    while queue:
        current_x, current_y, path = queue.popleft()

        if not in_bounds(current_x, current_y, pad):
            continue

        if (current_x, current_y) == (x2, y2):
            path_len = len(path)
            if path_len < shortest_len:
                shortest_len = path_len
                all_paths = [path]
            elif path_len == shortest_len:
                all_paths.append(path)
            continue

        visited[(current_x, current_y)].append(len(path))

        for _, (dx, dy) in directions.items():
            next_x, next_y = current_x + dx, current_y + dy
            if (next_x, next_y) not in visited or len(path) < min(visited[(next_x, next_y)]):
                new_path = path + [(next_x, next_y)]
                if len(new_path) <= shortest_len:
                    queue.append((next_x, next_y, new_path))
    return all_paths