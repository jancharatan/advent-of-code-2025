INPUT_FILE = "inputs/6.txt"

def main():
    ans = 0

    nums_lines = []
    operator_line = ""
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            if "+" not in line and "*" not in line:
                nums_lines.append(line.strip("\n"))
            else:
                operator_line = line.strip().split()
        
        breaks = [True for _ in range(len(nums_lines[0]))]
        for line in nums_lines:
            for i in range(len(line)):
                if line[i] != " ":
                    breaks[i] = False
        
        break_indices = []
        for i in range(len(breaks)):
            if breaks[i]:
                break_indices.append(i)
        break_indices.append(len(nums_lines[0]))
        
        curr = 0
        for i in range(len(break_indices)):
            nums = []
            while curr < break_indices[i]:
                num = ""
                for line in nums_lines:
                    num += line[curr]
                nums.append(int(num))
                curr += 1
            
            curr += 1
        
            if operator_line[i] == "+":
                ans += sum(nums)
            elif operator_line[i] == "*":
                prod = 1
                for num in nums:
                    prod *= num
                ans += prod

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
