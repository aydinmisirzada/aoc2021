from queue import PriorityQueue

INFINITY = 999999

def load_data(src):
    with open(src,'r') as f:
        matrix = []
        for line in f.readlines():
            line = line.strip()
            row = [int(c) for c in line]
            matrix.append(row)

    return matrix

def isValid(row, col, rows, cols):
    if (row < 0 or col < 0 or row >= rows or col >= cols):
        return False
 
    return True

#dijkstras algo
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def part1(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    dist = {}

    queue = PriorityQueue()
    processed = set()

    dist[(0,0)] = 0
    queue.put((0, (0, 0)))

    while not queue.empty():
        coord = queue.get()[1]
        if coord in processed:
            continue

        x,y = coord
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if (adjx,adjy) in processed:
                continue

            if (isValid(adjx, adjy, rows, cols)):
                alt = dist[coord] + matrix[adjx][adjy]
                if (adjx,adjy) not in dist or alt < dist[(adjx,adjy)]:
                    dist[(adjx,adjy)] = alt
                    queue.put((alt,(adjx,adjy)))

        processed.add(coord)

    return dist[(rows-1,cols-1)]


def part2(matrix):
    new_matrix= []

    #copy horizontally
    for row in matrix:
        new_row = []
        for i in range(5):
            new_row += [((x+i-1) % 9 + 1) for x in row]
            
        new_matrix.append(new_row)

    #copy vertically
    rows = len(new_matrix)
    for i in range(1,5):
        for row in range(rows):
            new_row = [((x+i-1) % 9 + 1) for x in new_matrix[row]]
            new_matrix.append(new_row)

    return part1(new_matrix)

if __name__ == '__main__':
    data = load_data('data.txt')
    print('Part 1:',part1(data))
    print('Part 2:',part2(data))
    