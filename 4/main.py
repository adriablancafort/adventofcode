def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    def search_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                # Check all 8 directions
                if search_direction(r, c, 0, 1):  # Horizontal right
                    count += 1
                if search_direction(r, c, 0, -1):  # Horizontal left
                    count += 1
                if search_direction(r, c, 1, 0):  # Vertical down
                    count += 1
                if search_direction(r, c, -1, 0):  # Vertical up
                    count += 1
                if search_direction(r, c, 1, 1):  # Diagonal down-right
                    count += 1
                if search_direction(r, c, 1, -1):  # Diagonal down-left
                    count += 1
                if search_direction(r, c, -1, 1):  # Diagonal up-right
                    count += 1
                if search_direction(r, c, -1, -1):  # Diagonal up-left
                    count += 1

    return count


def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            ul = grid[r-1][c-1]  # upper left
            ur = grid[r-1][c+1]  # upper right
            ll = grid[r+1][c-1]  # lower left
            lr = grid[r+1][c+1]  # lower right
            center = grid[r][c]
            
            if center != 'A':
                continue
                
            patterns = [
                (ul == 'M' and lr == 'S' and ur == 'M' and ll == 'S'),  # M-S and M-S
                (ul == 'S' and lr == 'M' and ur == 'S' and ll == 'M'),  # S-M and S-M
                (ul == 'M' and lr == 'S' and ur == 'S' and ll == 'M'),  # M-S and S-M
                (ul == 'S' and lr == 'M' and ur == 'M' and ll == 'S')   # S-M and M-S
            ]
            
            if any(patterns):
                count += 1
    
    return count


def read_input(filename):
    with open(filename, "r") as file:
        content = file.read()

    return content


def main():
    content = read_input("input.txt")
    grid = content.strip().split('\n')
    print("XMAS appeared: ", find_word(grid, "XMAS"))
    print("X-MAS appeared: ", find_xmas(grid))


if __name__ == "__main__":
    main()