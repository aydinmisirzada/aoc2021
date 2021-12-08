def load_data(src):
    with open(src,'r') as f:
        tmp = f.readlines()
        res = []
        for r in tmp:
            x = r.strip().split('|')
            x[0] = x[0].split()
            x[1] = x[1].split()
            res.append(x)

        return res

def solve(data):
    mapping = {2:'1',4:'4',3:'7',7:'8'}
    count = 0
    for row in data:
        for word in row[1]:
            if len(word) in mapping:
                # print(word)
                count += 1
    return count

if __name__ == '__main__':
    data = load_data('data.txt')
    result = solve(data)
    print(result)