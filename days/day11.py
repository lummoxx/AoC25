from collections import defaultdict
from functools import lru_cache
import sys
from utils import files

sys.setrecursionlimit(sys.getrecursionlimit()*1000000)

def traverse1(outputs, ends) -> set:
    paths = []

    @lru_cache(maxsize=None)
    def inner(start, path):
        path_list = list(path)
        path_list.append(start)
        path = tuple(path_list)
        next = outputs[start]
        if not next:
            paths.append(path)
        else:
            for n in next:
                paths.extend(inner(n,path))
        return set([p for p in paths  if p[-1] in ends])
    return len(inner("you", tuple()))

def traverse(outputs, ends) -> int:
    special = {"svr", "dac", "fft"}

    @lru_cache(maxsize=None)
    def dfs(start: str, target: str) -> int:
        total = 0
        for v in outputs.get(start, ()):
            if target == "":
                if v in ends:
                    total += 1
                elif v not in special:
                    total += dfs(v, target)
            else:
                if v == target:
                    total += 1
                elif v not in special:
                    total += dfs(v, target)
        return total

    c1 = dfs("svr", "dac")
    c2 = dfs("dac", "fft")
    c3 = dfs("fft", "")
    d1 = dfs("svr", "fft")
    d2 = dfs("fft", "dac")
    d3 = dfs("dac", "")

    return c1 * c2 * c3 + d1 * d2 * d3

def solve(ls):
    outputs = defaultdict(list)
    ends = []
    for line in ls:
        l = "".join(line).split(":")
        key = l[0]
        for output in l[1].split(" "):
            if output:
                if output == "out":
                    ends.append(key)
                else:
                    outputs[key].append(output)
    print(traverse1(outputs, ends))
    print(traverse(outputs, ends))

def main():
    day = 11
    real_lines = files.day_file(day)
    solve(real_lines)

if __name__ == '__main__':
    main()
