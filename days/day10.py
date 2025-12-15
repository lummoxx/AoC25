from collections import defaultdict
from functools import lru_cache
import itertools
from utils import files
import pulp

def solve(ls):
    count = 0
    count_2 = 0
    for l in ls:
        s = "".join(l)
        indicator_ligths = s[1:s.index("]")]
        bits = ["0" if ch == "." else "1" for ch in indicator_ligths]
        schematic_str = "".join(bits)
        s_mask = int(schematic_str, 2) if schematic_str else 0
        wiring = s[len(indicator_ligths)+3:s.index("{")-1].split(" ")
        buttons_1 = []
        buttons_2 = []
        for w in wiring:
            nums = list(map(int, w[1:-1].split(",")))
            buttons_2.append(nums)
            btn_bits = ["0"] * len(schematic_str)
            for num in nums:
                btn_bits[num] = "1"
            btn_str = "".join(btn_bits)
            buttons_1.append(int(btn_str, 2) if btn_str else 0)
        count += find_fastest_toggle(s_mask, buttons_1)
        j = s[s.index("{") + 1:s.index("}")]
        nums = list(map(int, j.split(",")))
        count_2 += increase_joltage_mip(nums, buttons_2)
    print(count)
    print(count_2)

def find_fastest_toggle(s: int, buttons: list) -> int:
    # if any((s ^ b) == 0 for b in buttons):
        # return 1

    n = len(buttons)
    for count in range(1, n + 1):
        for combo in itertools.combinations(buttons, count):
            xor = 0
            for v in combo:
                xor ^= v
            if xor == s:
                return count
    return n + 1

def increase_joltage_mip(target, buttons, fallback=True):
    L = len(target)
    btn_vecs = []
    for b in buttons:
        vec = [0] * L
        for i in b:
            if i < L:
                vec[i] += 1
        if any(vec):
            btn_vecs.append(tuple(vec))
    prob = pulp.LpProblem('increase_voltage', pulp.LpMinimize)
    xs = [pulp.LpVariable(f'x_{j}', lowBound=0, cat='Integer') for j in range(len(btn_vecs))]
    prob += pulp.lpSum(xs)
    for i in range(L):
        coeffs = [vec[i] for vec in btn_vecs]
        prob += (pulp.lpSum(xs[j] * coeffs[j] for j in range(len(coeffs))) == int(target[i]))
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    val = sum(int(pulp.value(x)) for x in xs)
    return val


def main():
    day = 10
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)
    solve(test_lines)
    solve(real_lines)

if __name__ == '__main__':
    main()
