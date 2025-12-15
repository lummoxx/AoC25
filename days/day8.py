from collections import defaultdict
import copy
import itertools
import math
from utils import files

def solve(ls, iterations):
    count = 0 
    points = []
    circuits = defaultdict(set)
    dists = defaultdict(list)
    
    for l in ls:
        l = "".join(l)
        [x, y, z] = l.split(",")
        points.append((int(x), int(y), int(z)))

    for (p1, p2) in itertools.combinations(points, 2):
        if p1 == p2:
            continue
        d = math.dist(p1, p2)
        dists[d] = [p1, p2]

    def connect():
        count2 = 0
        least = min(dists.keys())
        [p1, p2] = dists[least]
        if p2 not in circuits[p1]:
            for p in dists[least]:
                circuits[p] |= set(dists[least])

                for p2 in dists[least]:
                    circuits[p] |= circuits[p2]
                    circuits[p2] |= circuits[p]
                
                count = 0
                count2 = len(circuits[p])
                while (count2 > count):
                    ps = copy.deepcopy(circuits[p])
                    count = len(ps)
                    for p3 in ps:
                        circuits[p] |= circuits[p3]
                        circuits[p3] |= circuits[p]
                    count2 = len(circuits[p])
                
        del dists[least]
        return count2
    
    for c in range(0,iterations):
        connect()

    for _, c in circuits.items():
        for p2 in c:
            circuits[p2] |= c

    sizes = []
    counted = []
    for c in circuits.values():
        if not any([x in counted for x in c]):
            sizes.append(len(c))
            counted.extend(c)
    count = 1
    for i in sorted(sizes, reverse=True)[:3]:
        count *= i
    print(f"part 1: {count}")

    largest = 0
    while (largest < len(ls)):
        least = min(dists.keys())
        (x, _, _), (x1, _, _) = dists[least]
        largest = connect()
    print(f"part 2: {x * x1}")

    
def main():
    day = 8
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)
    solve(test_lines, 10)
    solve(real_lines, 1000)



if __name__ == '__main__':
    main()
