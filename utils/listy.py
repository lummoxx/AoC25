
import itertools


def group(ls : list, n : int) -> list :
    return [ls[i:i+n] for i in range(0, len(ls), n)]

def pair(indexes: list) -> list:
    pairs = []
    for pair in itertools.product(indexes, indexes):
        if pair[0]!=pair[1]:
            pairs.append(pair)
    return pairs

def ranges():
    cs1, cs2 = [1,5], [5, 9]
    c1, c2 = range(int(cs1[0]), int(cs1[1])+1), range(int(cs2[0]), int(cs2[1])+1)
    print(set(c1), set(c2))
    if set(c1).issubset(c2) or set(c2).issubset(c1):
        print("one fully contains the other!")