def parse_map(content: str):
    grid = [list(line) for line in content.strip().splitlines()]
    start_pos = None
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                start_pos = (x, y)
                break
        if start_pos:
            break
            
    return grid, start_pos


def get_next_position(pos, direction):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    return (pos[0] + dx[direction], pos[1] + dy[direction])


def is_valid_position(pos, grid) -> bool:
    if not (0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])):
        return False
    return grid[pos[1]][pos[0]] != '#'


def simulate_patrol(grid, start_pos):
    visited = {start_pos}
    pos = start_pos
    direction = 0
    
    states = {(start_pos, direction)}
    
    while True:
        next_pos = get_next_position(pos, direction)
        if (next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or 
            next_pos[1] < 0 or next_pos[1] >= len(grid)):
            break
        
        if grid[next_pos[1]][next_pos[0]] == '#':
            direction = (direction + 1) % 4
            
            state = (pos, direction)
            if state in states:
                break
            states.add(state)
            continue
            
        pos = next_pos
        visited.add(pos)
        
        state = (pos, direction)
        if state in states:
            break
        states.add(state)
    
    return len(visited)


def read_input(filename):
    with open(filename, "r") as file:
        content = file.read()

    return content


def main():
    content = read_input("input.txt")
    grid, start_pos = parse_map(content)
    result = simulate_patrol(grid, start_pos)
    print(f"The guard will visit {result} distinct positions.")


if __name__ == "__main__":
    main()