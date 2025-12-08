from math import sqrt

INPUT_FILE = "inputs/8.txt"
CONNECTIONS = 1000

def distance(a, b) -> float:
    x_d = (a[0] - b[0]) ** 2
    y_d = (a[1] - b[1]) ** 2
    z_d = (a[2] - b[2]) ** 2
    return sqrt(x_d + y_d + z_d)


def add_to_sets(sets: list[set], a, b) -> None:
    a_loc, b_loc = -1, -1
    for i, ls in enumerate(sets):
        if a in ls:
            a_loc = i
        if b in ls:
            b_loc = i
    
    if a_loc == -1 and b_loc == -1:
        s = set()
        s.add(a)
        s.add(b)
        sets.append(s)
    elif a_loc == -1:
        sets[b_loc].add(a)
    elif b_loc == -1:
        sets[a_loc].add(b)
    elif a_loc != b_loc:
        if a_loc > b_loc:
            a_set = sets.pop(a_loc)
            sets[b_loc] = sets[b_loc].union(a_set)
        else:
            b_set = sets.pop(b_loc)
            sets[a_loc] = sets[a_loc].union(b_set)


def main():
    sets = []
    points = []
    distances = []
    ans = 0
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            ls = l.strip().split(",")
            x, y, z = ls[0], ls[1], ls[2]
            points.append((int(x), int(y), int(z)))
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b = points[i], points[j]
                distances.append((points[i], points[j], distance(a, b)))

        distances.sort(key = lambda x : x[2])
        distances = distances[:CONNECTIONS]

        for (a, b, _) in distances:
            add_to_sets(sets, a, b)

        ans = 1
        circuit_sizes = list(sorted(map(lambda x: len(x), sets), key=lambda x: -x))[:3]
        for n in circuit_sizes:
            ans *= n       

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
