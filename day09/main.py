def load_data(src):
    with open(src,'r') as f:
        res = [list(i.strip()) for i in f.readlines()]
        for row in res:
            for i in range(len(row)):
                row[i] = int(row[i])
        return res

def part1(data):
    rows = len(data)
    cols = len(data[0])
    low_points = []

    for i in range(rows):
        for j in range(cols):
            above = data[i-1][j] if i > 0 else 10
            below = data[i+1][j] if i < (rows-1) else 10

            left = data[i][j-1] if j > 0 else 10
            right = data[i][j+1] if j < (cols-1) else 10

            adjacent = (left, right, above, below)
            adjacent = [a > data[i][j] for a in adjacent]

            if all(adjacent):
                low_points.append(data[i][j]+1)

    return sum(low_points)

dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def isValid(vis, row, col, matrix):
    rows = len(vis)
    cols = len(vis[0])

    if (row < 0 or col < 0 or row >= rows or col >= cols):
        return False

    if (matrix[row][col] >= 9):
        return False
 
    if (vis[row][col]):
        return False
 
    return True

def get_basins(i,j,matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    size_of_basin = 0

    visited = [[False] * cols for i in range(rows)]

    queue = []

    queue.append((i,j))
    visited[i][j] = True

    while queue:

        x, y = queue.pop(0)
        print((x,y))
        size_of_basin += 1

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(visited, adjx, adjy, matrix)):
                queue.append((adjx, adjy))
                visited[adjx][adjy] = True

    return size_of_basin

def part2(data):
    rows = len(data)
    cols = len(data[0])
    low_points = [[0] * cols for i in range(rows)]
    basins = []

    #get low points
    for i in range(rows):
        for j in range(cols):
            above = data[i-1][j] if i > 0 else 10
            below = data[i+1][j] if i < (rows-1) else 10

            left = data[i][j-1] if j > 0 else 10
            right = data[i][j+1] if j < (cols-1) else 10

            adjacent = (left, right, above, below)
            adjacent = [a > data[i][j] for a in adjacent]

            if all(adjacent):
                low_points[i][j] = 1

    for i in range(rows):
        for j in range(cols):
            if low_points[i][j] > 0:
                basins.append(get_basins(i,j,data))
                print('--------')

    basins.sort()
    prod = 1
    for i in basins[-3:]:
        prod *= i
    return prod

if __name__ == '__main__':
    data = load_data('data.txt')
    print(part2(data))