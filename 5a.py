INPUT_FILE = "inputs/5.txt"

def main():
    ans = 0

    ranges, nums = [], []
    has_reached_nums = False
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            if l.strip() == "":
                has_reached_nums = True
                continue

            if not has_reached_nums:
                range_ls = l.strip().split("-")
                ranges.append((int(range_ls[0]), int(range_ls[1])))
            else:
                nums.append(int(l.strip()))
        
        for num in nums:
            for (start, end) in ranges:
                if start <= num and num <= end:
                    ans += 1
                    break
    
    print(f"The answer is {ans}.")



if __name__ == "__main__":
    main()
