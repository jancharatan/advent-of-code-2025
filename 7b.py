INPUT_FILE = "inputs/7.txt"

def main():
    curr = set()
    splitters = []
    with open(INPUT_FILE) as f:
        start = f.readline()
        start_index = start.find("S")
        curr.add(start_index)

        for l in f.readlines():
            if "^" in l:
                splitters.append([])
            for i in range(len(l)):
                if l[i] == "^":
                    splitters[-1].append(i)
    
    paths = { start_index: 1 }
    for level in splitters:
        for split_index in level:
            if split_index not in paths:
                continue

            if split_index - 1 in paths:
                paths[split_index - 1] += paths[split_index]
            else:
                paths[split_index - 1] = paths[split_index]

            if split_index + 1 in paths:
                paths[split_index + 1] += paths[split_index]
            else:
                paths[split_index + 1] = paths[split_index]

            paths[split_index] = 0

    print(f"The answer is {sum(paths.values())}.")


if __name__ == "__main__":
    main()
