INPUT_FILE = "inputs/3.txt"


def remove_char(s: str) -> int:
    for i in range(len(s)):
        if i == len(s) - 1:
            return i
        elif int(s[i]) < int(s[i + 1]):
            return i


def get_max_joltage(s: str) -> int:
    while len(s) > 12:
        i = remove_char(s)
        s = s[:i] + s[i+1:]
    return int(s)


def main():
    ans = 0
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            ans += get_max_joltage(l.strip())
    
    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
