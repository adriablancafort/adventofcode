def read_input(filename):
    with open(filename, "r") as file:
        content = file.read().strip()
    
    rules_section, updates_section = content.split("\n\n")
    
    rules = []
    for line in rules_section.split("\n"):
        before, after = line.split("|")
        rules.append((int(before), int(after)))
    
    updates = []
    for line in updates_section.split("\n"):
        updates.append([int(x) for x in line.split(",")])
    
    return rules, updates


def topological_sort(pages, rules):
    graph = {page: set() for page in pages}
    in_degree = {page: 0 for page in pages}
    
    for before, after in rules:
        if before in pages and after in pages:
            graph[before].add(after)
            in_degree[after] += 1
    
    queue = [page for page, degree in in_degree.items() if degree == 0]
    result = []
    
    while queue:
        page = min(queue)
        queue.remove(page)
        result.append(page)
        
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result


def get_middle_number(sequence):
    return sequence[len(sequence) // 2]


def is_valid_order(update, rules):
    sorted_update = topological_sort(set(update), rules)
    return update == sorted_update


def solve_part1(rules, updates):
    return sum(
        get_middle_number(update)
        for update in updates
        if is_valid_order(update, rules)
    )


def solve_part2(rules, updates):
    return sum(
        get_middle_number(topological_sort(set(update), rules))
        for update in updates
        if not is_valid_order(update, rules)
    )


def main():
    rules, updates = read_input("input.txt")

    print("Part 1:", solve_part1(rules, updates))
    
    print("Part 2:", solve_part2(rules, updates))


if __name__ == "__main__":
    main()