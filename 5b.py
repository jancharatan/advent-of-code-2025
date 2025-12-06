INPUT_FILE = "inputs/5.txt"

def main():
    seen = set()
    ranges = []
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            if l.strip() == "":
                break

            range_ls = l.strip().split("-")
            start = int(range_ls[0])
            end = int(range_ls[1])
            ranges.append([start, end])

    ranges.sort(key = lambda x: x[0])

    merged_ranges = [ranges[0]]
    for (start, end) in ranges[1:]:
        if (start <= merged_ranges[-1][1]):
            merged_ranges[-1][1] = max(end, merged_ranges[-1][1])
        else:
            merged_ranges.append([start, end])
    
    ans = 0
    for (start, end) in merged_ranges:
        ans += end - start + 1    

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
