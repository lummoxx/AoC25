from typing import Callable
from utils import files
from utils import listy

def invalid(s: str) -> bool:
    m = len(s)//2
    return s[:m] == s[m:]

def invalid_2(s: str) -> bool:
    for i in range(1, len(s)//2 + 1):
        nums = listy.group(list(s), i)
        if all(x == nums[0] for x in nums):
            return True
    return False


def solve(input_str: str, pred: Callable[[str], bool]) -> int:
    invalids = 0
    ranges = input_str.split(',')
    for r in ranges:
        bounds = r.split('-')
        start, end = bounds[0], bounds[1]
        for i in range(int(start), int(end)+1):
            if pred(str(i)):
                invalids += i
    print(invalids)

def main():
    day = 2
    real_lines = files.str_day(day)
    solve(real_lines, lambda s: invalid(s))
    solve(real_lines, lambda s: invalid(s) or invalid_2(s))

if __name__ == '__main__':
    main()
