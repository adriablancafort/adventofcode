def check_levels(levels):
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))

    return increasing or decreasing


def is_safe(report):
    levels = list(map(int, report.split()))
    return check_levels(levels)


def is_safe_dampener(report):
    levels = list(map(int, report.split()))

    if check_levels(levels):
        return True

    for i in range(len(levels)):
        if check_levels(levels[:i] + levels[i+1:]):
            return True

    return False


def count_safe_reports(content):
    lines = content.strip().split('\n')
    
    safe_reports = sum(1 for line in lines if is_safe(line))

    return safe_reports


def count_safe_reports_dampener(content):
    lines = content.strip().split('\n')
    
    safe_reports = sum(1 for line in lines if is_safe_dampener(line))

    return safe_reports


def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content


def main():
    content = read_input('input.txt')
    print("Safe reports:", count_safe_reports(content))
    print("Safe reports dampener:", count_safe_reports_dampener(content))


if __name__ == '__main__':
    main()