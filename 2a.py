START = 50
INPUT_FILE = "inputs/2.txt"


def is_valid_id(i: int) -> bool:
    id = str(i)
    l = len(id)

    return id[:l//2] != id[l//2:]


def main():
    ans = 0
    with open(INPUT_FILE) as f:
        ranges = f.readline().strip().split(",")
        for s in ranges:
            s_split = s.split("-")
            id_1, id_2 = s_split[0], s_split[1]
            
            for i in range(int(id_1), int(id_2) + 1):
                if not is_valid_id(i):
                    ans += int(i)
        
        print(f"The answer is {ans}.")




if __name__ == "__main__":
    main()
