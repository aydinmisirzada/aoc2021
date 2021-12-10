import statistics

def load_data(src):
    with open(src,'r') as f:
        res = [i.strip() for i in f.readlines()]
        return res

def part1(data):
    stack = []
    chars = {'{':'}',
            '[':']',
            '<':'>',
            '(':')'
            }

    points = {')':3,
            ']':57,
            '}':1197,
            '>':25137
            }
    mistakes = []

    for line in data:
        stack = []
        for c in line:
            if c in chars:
                stack.append(c)
            else:
                current_c = stack.pop()
                if c != chars[current_c]:
                    mistakes.append(c)
                    break

    return sum([points[m] for m in mistakes])

def part2(data):
    stack = []
    chars = {'{':'}',
            '[':']',
            '<':'>',
            '(':')'
            }

    points = {')':1,
            ']':2,
            '}':3,
            '>':4
            }
    corrections = []
    correction_points = []
    WAS_CORRUPT_LINE = False

    for line in data:
        stack = []
        for c in line:
            if c in chars:
                stack.append(c)
            else:
                current_c = stack.pop()
                if c != chars[current_c]:
                    WAS_CORRUPT_LINE = True
                    break
        if WAS_CORRUPT_LINE:
            WAS_CORRUPT_LINE = False
        else:
            stack.reverse()
            corrections = [chars[i] for i in stack]
            
            the_sum = 0
            for correction in corrections:
                the_sum *= 5
                the_sum += points[correction]
            correction_points.append(the_sum)


    return statistics.median(correction_points)


if __name__ == '__main__':
    data = load_data('data.txt')
    result = part2(data)
    print(result)