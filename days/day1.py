from utils import files

start = 50

def solve_part_1(lines):
    current = start
    zeroes = 0
    for l in lines:
        rotate = int("".join(l[1:]))
        if l[0] == 'L':
            current -= rotate
            while current < 0:
                current += 100
        else:
            current += rotate
            while current > 99:
                current -= 100
        if current == 0:
            zeroes += 1
    return zeroes

def solve_part_2(lines):
    current = start
    zeroes = 0
    for l in lines:
        rotate = int("".join(l[1:]))
        zeroes += rotate // 100
        rotate = rotate % 100
        if l[0] == 'L':
            if current > 0 and rotate >= current:
                zeroes += 1
            current -= rotate
            if current < 0:
                current += 100
        else:
            current += rotate
            if current > 99:
                current -= 100
                zeroes += 1
    return zeroes


def main():
    day = 1
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)

    print(solve_part_1(real_lines))
    print(solve_part_2(real_lines))

if __name__ == '__main__':
    main()
