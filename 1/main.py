def calculate_total_distance(content):
    lines = content.strip().split('\n')

    left_list = []
    right_list = []

    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list)))
    
    return total_distance


def calculate_similarity_score(content):
    lines = content.strip().split('\n')

    left_list = []
    right_list = []

    for line in lines:
        left, right = map(int, line.split()[:2])
        left_list.append(left)
        right_list.append(right)
    
    similarity_score = 0
    for left in left_list:
        count = right_list.count(left)
        similarity_score += left * count
    
    return similarity_score


def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content


def main():
    content = read_input('input.txt')
    print("Total distance: ", calculate_total_distance(content))
    print("Similarity score: ", calculate_similarity_score(content))


if __name__ == '__main__':
    main()