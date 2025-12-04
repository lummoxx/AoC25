import copy
from utils import files
from utils import listy
import string

def remove_first_smallest(ls: list):
    for i in range(0, len(ls) - 1):
        if ls[i] < ls[i+1] or ls[i] == min(ls):
            ls = ls[:i] + ls[i+1:]
            return ls
    ls.remove(min(ls))
    return ls


def help(ls: list):
    bank = list(map(int, ls))
    last_start = len(bank) - 12
    possible_starts = bank[:last_start-1]
    max_val = max(possible_starts)
    start = bank.index(max_val)
    jolt = bank[start:]
    while (len(jolt) > 12):
        jolt = remove_first_smallest(jolt)
    jolt = int(''.join(map(str, jolt)))
    return jolt
    
    
def solve2(banks: list):
    sum = 0
    for bank in banks:
        sum += help(bank)
    print(sum)


def solve1(banks: list):
    sum_jolt = 0
    for bank in banks:
        max1 = 0
        max2 = 0
        for i, jolt_str in enumerate(bank):
            jolt = int(jolt_str)
            if i < len(bank) - 1 and jolt > max1:
                max1 = jolt
                max2 = int(bank[i+1])
            else:
                if jolt > max2:
                    max2 = jolt
        sum_jolt += int("".join([str(max1),str(max2)]))
    print(sum_jolt)

def main():
    day = 3
    test_banks = files.test_file(day)
    real_banks = files.day_file(day)
    solve2(test_banks)
    solve2(real_banks)


if __name__ == '__main__':
    main()
