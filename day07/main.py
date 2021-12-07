import statistics

def load_data(src):
    with open(src,'r') as f:
        return [int(i) for i in f.readline().strip().split(',')]

def sum_to_n(n):
    return n*(n+1) // 2

def part1(data):
    """
    >>> part1([16,1,2,0,4,2,7,1,2,14])
    37
    """

    target = int(statistics.median(data))
    result = sum([abs(i - target) for i in data])

    return result



def part2(data):
    """
    >>> part2([16,1,2,0,4,2,7,1,2,14])
    168
    """

    target = max(data)
    min_sum = 9999999999
    for i in range(target):
        moves = []
        for j in data:
            moves_needed = abs(j - i)
            moves_needed  = sum_to_n(moves_needed)
            moves.append(moves_needed)

        current_sum = sum(moves)

        if current_sum < min_sum:
            min_sum = current_sum

    return min_sum

if __name__ == '__main__':
    data = load_data('data.txt')
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))