START = 50
INPUT_FILE = "inputs/2.txt"  


def is_length_valid(i: int, length: int) -> bool:
    s = str(i)

    compare_to = s[:length]
    for i in range(length, len(s), length):
        if compare_to != s[i:i+length]:
            return True
    return False



def is_valid_id(i: int) -> bool:
    for length in range(1, len(str(i))):
        if not is_length_valid(i, length):
            return False
    return True


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
