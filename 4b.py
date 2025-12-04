INPUT_FILE = "inputs/4.txt"


def remove_rolls(grid: list[list[str]]) -> int:
    removed = 0
    width, height = len(grid[0]), len(grid)
    to_remove = set()
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "@":
                count = 0
                for (x, y) in [(-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (1, -1), (-1, 1)]:
                    if 0 <= i + x < height and 0 <= j + y < width and grid[i + x][j + y] == "@":
                        count += 1
                    if count == 4:
                        break
                
                if count < 4:
                    removed += 1
                    to_remove.add((i, j))
    
    for (i, j) in to_remove:
        grid[i][j] = "."

    return removed


def main():
    ans = 0
    with open(INPUT_FILE) as f:
        grid = []
        for l in f.readlines():
            grid.append([c for c in l.strip()])
    
    removed = -1
    while removed != 0:
        removed = remove_rolls(grid)
        ans += removed

    print(f"The answer is {ans}.")


if __name__ == "__main__":
    main()
