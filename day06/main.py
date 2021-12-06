def load_data(src):
    with open(src,'r') as f:
        line = f.readline().strip().split(',')
        return [int(i) for i in line]


def solve(data, days=80):
    """
    >>> solve([3, 4, 3, 1, 2], days=18)
    26

    >>> solve([3, 4, 3, 1, 2])
    5934
    """

    fishes = [0] * 9

    for fish in data:
        fishes[fish] += 1

    for day in range(days):
        next_day = [0] * 9
        for fish, count in enumerate(fishes):
            if fish > 0:
                next_day[fish - 1] += count
            else:
                next_day[6] += count
                next_day[8] += count

        fishes = next_day

    return sum(fishes)
         

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    data = load_data('data.txt')
    result = solve(data)
    print(result)