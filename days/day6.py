from utils import files

ops = {"+": lambda x, y: x + y, "*": lambda x, y: x* y}

def eval(x:int, y:int, op: str)->int:
    return ops[op](x, y)

def solve(ls: list):
    count = 0
    operators = ls[-1].split(" ")
    operators = [x for x in operators if x != ""]
    columns = []
    for l in ls[:-1]:
        nums = list(map(lambda x: x.strip(), l.split(" ")))
        nums = [int(x) for x in nums if x != ""]
        columns.append(nums)
    for i in range(0,len(operators)):
        summa = eval(columns[0][i], columns[1][i], operators[i])
        n = 2
        while (n < len(columns)):
            summa = eval(summa, columns[n][i], operators[i])
            n += 1
        count += summa
    print(count)


def solve2(ls: list):
    count = 0
    columns = []
    i = 0
    while(i < len(ls[-1])):
        op = []
        if (x := ls[-1][i]) != " ":
            op.append(x)
            i += 1
            while( i < len(ls[-1])  and (x := ls[-1][i]) == " "):
                op.append(x)
                i+= 1
            columns.append(op)
    nums = [list(x[0]) for x in columns]

    for l in ls[:-1]:
        start = 0
        for i, c in enumerate(columns):
            if (start+len(c) < len(l)):
                nums[i].append(l[start:start+len(c)-1])
            else:
                nums[i].append(l[start:start+len(c)])
            start += len(c)

    for n in nums:
        op, ls = n[0], n[1:]
        ns = []
        m = len(max(ls,key=len))
        while(m):
            vs = []
            for x in ls:
                i = ls.index(x)
                if(x != " "):
                    vs.append(x[-1])
                x = x[:-1]
                ls[i] = x
            ns.append("".join(vs))
            m = len(max(ls,key=len))
        summa = int(ns[0])
        for t in ns[1:]:
            summa = eval(summa, int(t), op)
        count +=  summa
    print(count)


def main():
    day = 6
    input = files.day_file(day)
    solve(input)
    solve2(input)


if __name__ == '__main__':
    main()
