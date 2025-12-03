INPUT_FILE = "inputs/3.txt"

def get_largest_int(s: str) -> (str, int):
    for candidate in ["9", "8", "7", "6", "5", "4", "3", "2", "1"]:
        idx = s.find(candidate)
        if idx != -1:
            return (candidate, idx)
    
    return (-1, "0")
    

def get_max_joltage(s: str) -> int:
    i_1, idx = get_largest_int(s[:-1])
    i_2, _ = get_largest_int(s[idx+1:])
    return int(i_1 + i_2)


def main():
    ans = 0
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            ans += get_max_joltage(l.strip())
    
    print(f"The answer is {ans}.")



if __name__ == "__main__":
    main()
