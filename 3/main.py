import re

def sum_mul(content):
    pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    
    matches = pattern.findall(content)
    
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum


def sum_mul_do(content):
    mul_pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    total_sum = 0
    mul_enabled = True
    i = 0

    while i < len(content):
        if mul_enabled:
            mul_match = mul_pattern.match(content, i)
            if mul_match:
                x, y = mul_match.groups()
                total_sum += int(x) * int(y)
                i = mul_match.end()
                continue

        do_match = do_pattern.match(content, i)
        if do_match:
            mul_enabled = True
            i = do_match.end()
            continue

        dont_match = dont_pattern.match(content, i)
        if dont_match:
            mul_enabled = False
            i = dont_match.end()
            continue

        i += 1

    return total_sum


def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content


def main():
    content = read_input('input.txt')
    print("Sum mul:", sum_mul(content))
    print("Sum mul do:", sum_mul_do(content))


if __name__ == '__main__':
    main()