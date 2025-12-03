START = 50
INPUT_FILE = "inputs/1a.txt"

def main():
    ans = 0
    curr = START
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            direction, scale = l[0], int(l[1:])

            if direction == "L":
                curr -= scale
            elif direction == "R":
                curr += scale
            
            curr %= 100

            if curr < 0:
                curr += 100
            
            if curr == 0:
                ans += 1
    
    print(f"The answer is {ans}.")



if __name__ == "__main__":
    main()
