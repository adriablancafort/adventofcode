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


def simulate_guard(grid, start_pos):
    steps = set()
    direction = 0
    current_pos = (start_pos[1], start_pos[0])  

    while True:
        if direction == 0:  # North
            next_pos = (current_pos[0] - 1, current_pos[1])
        elif direction == 1:  # East
            next_pos = (current_pos[0], current_pos[1] + 1)
        elif direction == 2:  # South
            next_pos = (current_pos[0] + 1, current_pos[1])
        else:  # West
            next_pos = (current_pos[0], current_pos[1] - 1)
        
        if (next_pos[0] < 0 or next_pos[1] < 0 or 
            next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0])):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            direction = (direction + 1) % 4
        elif current_pos + next_pos in steps:
            return True
        else:
            steps.add(current_pos + next_pos)
            current_pos = next_pos

    return False


def count_loop_obstructions(grid, start_pos):
    loop_count = 0
    start_pos = (start_pos[1], start_pos[0])
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                continue
                
            original_val = grid[y][x]
            grid[y][x] = '#'
            
            if simulate_guard(grid, start_pos):
                loop_count += 1
                
            grid[y][x] = original_val
    
    return loop_count


def read_input(filename):
    with open(filename, "r") as file:
        content = file.read()

    return content


def main():
    content = read_input("input.txt")
    grid, start_pos = parse_map(content)
    print("Distinct positions visited by the guard:", simulate_patrol(grid, start_pos))
    print("Number of positions for new obstructions to cause loops:", count_loop_obstructions(grid, start_pos))


if __name__ == "__main__":
    main()