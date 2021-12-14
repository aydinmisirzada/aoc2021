def load_data(src):
    with open(src,'r') as f:
        reading = 'coords'
        data = ([],[])
        max_x, max_y = 0, 0
        for line in f.readlines(): 
            line = line.strip()
            if not line:
                reading = 'folds'
                continue

            if reading == 'coords':
                x, y = line.split(',')
                x, y = int(x), int(y)
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y

                data[0].append((x,y))

            else:
                line = line[len('fold along '):]
                a, b = line.split('=')
                data[1].append((a, int(b)))

        matrix = [['.' for x in range(max_x+1)] for y in range(max_y+1)]

        for coord in data[0]:
            matrix[coord[1]][coord[0]] = '#'

        return matrix, data[1]

def fold_horizontally(matrix, line):
    res = []
    for i in range(line):
        up, bottom = matrix[i], matrix[-1 - i]
        tmp = []
        for j in range(len(up)):
            if up[j] == '#' or bottom[j] == '#':
                tmp.append('#')
            else:
                tmp.append('.')
        res.append(tmp)

    return res

def fold_vertically(matrix, border):
    res = []
    for line in matrix:
        tmp = []
        for i in range(border):
            if line[i] == '#' or line[-1-i] == '#':
                tmp.append('#')
            else:
                tmp.append('.')
        res.append(tmp)

    return res

def part1(matrix, folds):
    res = matrix.copy()
    the_sum = 0
    fold = folds[0]
    if fold[0] == 'y':
        res = fold_horizontally(res, int(fold[1]))
    else:
        res = fold_vertically(res, int(fold[1]))

    for line in res:
        the_sum += line.count('#')

    return the_sum

def part2(matrix, folds):
    res = matrix.copy()
    for fold in folds:
        if fold[0] == 'y':
            res = fold_horizontally(res, int(fold[1]))
        else:
            res = fold_vertically(res, int(fold[1]))

    for line in res:
        print(' '.join(line))

if __name__ == '__main__':
    matrix, folds = load_data('data.txt')
    result = part1(matrix, folds)
    print('Part 1:',result)
    print('Part 2:')
    part2(matrix, folds)
