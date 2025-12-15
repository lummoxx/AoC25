from functools import lru_cache
from utils import files

def fits(region, shapes):
    [x,y] = region[0]
    to_fit = [(i,n) for (i,n) in enumerate(region[1]) if n > 0]
    size = sum([sum([y.count('#') for y in shapes[i]])*n for (i,n) in to_fit])
    if size > x*y:
        return False
    return True

def solve(ls):
    count = 0
    gs = ls.split("\n\n")
    regions = []
    rs = gs[-1].split("\n")
    for r in rs:
        region = r.split(" ")
        dimensions = region[0].split(":")[0]
        regions.append((list(map(int, dimensions.split("x"))), list(map(int, region[1:]))))

    shapes = []
    for s in gs[:-1]:
        r = s.split("\n")
        shapes.append(r[1:])
    
    for r in regions:
        if fits(r, shapes):
            count += 1
    print(count)

def main():
    day = 12
    real_str = files.str_day(day)
    solve(real_str)

if __name__ == '__main__':
    main()
