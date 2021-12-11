def load_data(src):
    with open(src,'r') as f:
        res = [list(i.strip()) for i in f.readlines()]
        for row in res:
            for i in range(len(row)):
                row[i] = int(row[i])
        return res

dRow = [ -1, 0, 1, 0, -1, -1, 1, 1]
dCol = [ 0, 1, 0, -1, -1, 1, -1, 1]

def isValid(vis, row, col):
    rows = len(vis)
    cols = len(vis[0])

    if (row < 0 or col < 0 or row >= rows or col >= cols):
        return False

    if (vis[row][col]):
        return False
 
    return True

def spread_the_light(i,j,matrix, flashers, visited):
    queue = []

    queue.append((i,j))

    visited[i][j] = True

    while queue:

        x, y = queue.pop(0)

        #grabbing the adjacents
        for i in range(8):
            adjx = x + dRow[i]
            adjy = y + dCol[i]

            if (isValid(visited, adjx, adjy)):
                matrix[adjx][adjy] += 1

                if matrix[adjx][adjy] > 9 and (adjx,adjy) not in flashers:
                    queue.append((adjx, adjy))
                    flashers.add((adjx, adjy))

        visited[x][y] = True
        

def solve(matrix):
    rows = len(data)
    cols = len(data[0])

    counter = 0
    sum_of_flashers = 0
    while(True):
        flashers = set()
        visited = [[False] * cols for i in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
    
                matrix[i][j] += 1

                if matrix[i][j] > 9:
                    flashers.add((i,j))

        for (i,j) in flashers.copy():
            spread_the_light(i,j,matrix,flashers, visited)

        for (i,j) in flashers:
            matrix[i][j] = 0

        if len(flashers) == 100:
            break

        counter +=1

        if (counter<=100):
            sum_of_flashers += len(flashers)


    return counter+1, sum_of_flashers

if __name__ == '__main__':
    data = load_data('data.txt')
    result = solve(data)
    print('Part 1:',result[0])
    print('Part 2:',result[1])