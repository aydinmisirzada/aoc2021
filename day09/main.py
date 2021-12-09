def load_data(src):
    with open(src,'r') as f:
        res = [list(i.strip()) for i in f.readlines()]
        for row in res:
            for i in range(len(row)):
                row[i] = int(row[i])
        return res

def solve(data):
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

if __name__ == '__main__':
    data = load_data('data.txt')
    print(solve(data))