INPUT_FILE = "inputs/6.txt"

def main():
    ans = 0

    nums = {}
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            if "+" not in line and "*" not in line:
                line_nums = line.strip().split()
                for i in range(len(line_nums)):
                    if i in nums:
                        nums[i].append(int(line_nums[i]))
                    else:
                        nums[i] = [int(line_nums[i])]
            else:
                operators = line.strip().split()
                for i in range(len(operators)):
                    if operators[i] == "+":
                        ans += sum(nums[i])
                    elif operators[i] == "*":
                        prod = 1
                        for num in nums[i]:
                            prod *= num
                        ans += prod

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
