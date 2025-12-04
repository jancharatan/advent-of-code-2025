INPUT_FILE = "inputs/4.txt"


def main():
    ans = 0
    with open(INPUT_FILE) as f:
        grid = []
        for l in f.readlines():
            grid.append([c for c in l.strip()])
    
    
    width, height = len(grid[0]), len(grid)
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
                    ans += 1
    
    print(f"The answer is {ans}.")



if __name__ == "__main__":
    main()
