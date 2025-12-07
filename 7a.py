INPUT_FILE = "inputs/7.txt"

def main():
    curr = set()
    ans = 0
    with open(INPUT_FILE) as f:
        start = f.readline()
        curr.add(start.find("S"))

        for l in f.readlines():
            for i in range(len(l)):
                if l[i] == "^" and i in curr:
                    curr.remove(i)
                    curr.add(i - 1)
                    curr.add(i + 1)
                    ans += 1
            
            

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
