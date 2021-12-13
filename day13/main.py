def load_data(src):
    tmp = []
    with open(src,'r') as f:
        max_x = 0
        max_y = 0
        lines = f.readlines()
        empty_line = 0
        for index, line in enumerate(lines): 
            if line=='\n':
                empty_line = index
                break
            x, y = line.strip().split(',')
            x, y = int(x), int(y)
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y

            tmp.append((x,y))
        
        folds = []
        for i in range(empty_line+1, len(lines)):
            folds.append(lines[i].strip().split()[2].split('='))

        matrix = [['.' for x in range(max_x+1)] for i in range(max_y+1)]
        x = 0
        y = 1
        for coord in tmp:
            matrix[coord[y]][coord[x]] = '#'
        return matrix, folds

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
