INPUT_FILE = "inputs/9.txt"

def main():
    ans = 0
    with open(INPUT_FILE) as f:
        points = []
        for l in f.readlines():
            l_split = l.strip().split(",")
            x, y = int(l_split[0]), int(l_split[1])
            points.append((x, y))

        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                area = abs(points[i][0] - points[j][0] + 1) * abs(points[i][1] - points[j][1] + 1)
                ans = max(ans, area)

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
