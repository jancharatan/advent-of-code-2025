START = 50
INPUT_FILE = "inputs/1.txt"

def main():
    ans = 0
    curr = START
    with open(INPUT_FILE) as f:
        for l in f.readlines():
            direction, scale = l[0], int(l[1:])

            if scale > 100:
                ans += scale // 100

            remainder = scale % 100

            start = curr
            if direction == "L":
                
                if start != 0 and curr - remainder <= 0:
                    ans += 1

                curr -= scale

            elif direction == "R":
                if start != 0 and curr + remainder >= 100:
                    ans += 1

                curr += scale

            curr %= 100
            print(curr, ans)

    print(f"The answer is {ans}.")



if __name__ == "__main__":
    main()
