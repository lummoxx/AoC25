from utils import files


roll = "@"
empty = "."
adjacent = [(1,0), (0,-1), (0,1),(-1,0), (-1,-1), (1,1), (-1, 1), (1, -1)]

def solve(grid: list):
    count = 0
    to_remove = []
    for x, line in list(enumerate(grid)):
        for y, r in list(enumerate(line)):
            if r == roll:
                neighbours = 0
                for dx, dy in adjacent:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < len(grid) and y + dy < len(line):
                        if grid[x+dx][y+dy] == roll:
                            neighbours += 1
                if neighbours < 4:
                    count += 1
                    to_remove.append((x,y))
    for x, y in to_remove:
        grid[x][y] = empty
    return count, grid




def main():
    day = 4
    grid = files.day_file(day)
    count = 0
    c = 1
    while c > 0:
        c, grid = solve(grid)
        c2, grid = solve(grid)
        count += c + c2
    print(count)


if __name__ == '__main__':
    main()
