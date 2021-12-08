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

def decode(patterns):
    digits = {}

    digits[1] = next(filter(lambda x: len(x) == 2, patterns),None)
    digits[4] = next(filter(lambda x: len(x) == 4, patterns), None)
    digits[7] = next(filter(lambda x: len(x) == 3, patterns), None)
    digits[8] = next(filter(lambda x: len(x) == 7, patterns), None)

    six_segmenters = set(filter(lambda x: len(x) == 6, patterns))
    known_six_segmenters = set()

    digits[6] = next(filter(lambda x: digits[1][0] not in x or digits[1][1] not in x, six_segmenters), None)
    digits[9] = next(filter(lambda x: set(digits[4]) <= set(x), six_segmenters), None)

    known_six_segmenters.add(digits[6])
    known_six_segmenters.add(digits[9])
    digits[0] = six_segmenters.difference(known_six_segmenters).pop()

    five_segmenters = set(filter(lambda x: len(x) == 5, patterns))
    known_five_segmenters = set()

    digits[3] = next(filter(lambda x: set(digits[1]) <= set(x), five_segmenters), None)

    digits[5] = next(filter(lambda x: set(x) <= set(digits[9]) and x != digits[3], five_segmenters), None)
    
    known_five_segmenters.add(digits[5])
    known_five_segmenters.add(digits[3])

    digits[2] = five_segmenters.difference(known_five_segmenters).pop()

    for key, value in digits.items():
        tmp = ''.join(sorted(value))
        digits[key] = tmp

    return dict((v,k) for k,v in digits.items())

def get_digit(output, mapping):
    return mapping.keys()[output] 

def part2(data):
    the_sum = 0

    for entry in data:

        patterns = entry[0]

        mapping = decode(patterns)


        output = entry[1]

        num = 0

        for o in output:
            tmp = ''.join(sorted(o))

            if tmp in mapping:
                num += int(mapping[tmp])
                num *= 10

        num = num // 10
        the_sum += num 
        print(num)

    return the_sum


if __name__ == '__main__':
    data = load_data('data.txt')
    result = part2(data)
    print('----')
    print(result)