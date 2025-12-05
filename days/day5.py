from utils import files

def solve1(ls: list):
    fresh = 0
    ranges = []
    ingredients = []

    for l in ls:
        if "-" in l:
            ranges.append(list(map(int, l.split("-"))))
        else:
            if l != "":
                ingredients.append(int(l))

    for i in ingredients:
        for range in ranges:
            if i >= range[0] and i <= range[1]:
                fresh += 1
                break
    print(fresh)


def solve2(ls: list):
    ranges = []
    minimised = set()
    count = 0

    for l in ls:
        if "-" in l:
            ranges.append(tuple(map(int, l.split("-"))))
        else:
            break

    previous_upper = 0
    for r in sorted(ranges):
        if previous_upper <= r[1]:
            minimised.add((max(previous_upper, r[0]), r[1]))
            previous_upper = r[1] + 1
    for r in minimised:
        count += r[1] - r[0] + 1
    print(count)


def main():
    day = 5
    test_lines = files.test_file(day)
    real_lines = files.day_file(day)
    solve2(real_lines)


if __name__ == '__main__':
    main()
