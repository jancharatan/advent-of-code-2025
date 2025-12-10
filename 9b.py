from collections import defaultdict

INPUT_FILE = "inputs/9.txt"

def is_square_valid(points: list[(int, int)], i: int, valid_rows) -> bool:
    (ax, ay) = points[i]
    (bx, by) = points[i + 1]
    (cx, cy) = points[i + 2]

    x = cx if ax == bx else ax
    y = cy if ay == by else ay

    if y not in valid_rows:
        return False
    
    for a, b in valid_rows[y]:
        if a <= x <= b:
            return True
    return False



def main():
    ans = max_x = max_y = 0
    with open(INPUT_FILE) as f:
        points = []
        for l in f.readlines():
            l_split = l.strip().split(",")
            x, y = int(l_split[0]), int(l_split[1])
            max_x, max_y = max(x, max_x), max(y, max_y)
            points.append((x, y))
        points.append(points[0])
        points.append(points[1])
    
        valid_rows = defaultdict(list)

        n = len(points)
        for i in range(n - 2):
            if not is_square_valid(points, i, valid_rows):
                continue

            x_l = abs(points[i][0] - points[i + 2][0]) + 1
            y_l = abs(points[i][1] - points[i + 2][1]) + 1
            area = x_l * y_l
            ans = max(area, ans)

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
