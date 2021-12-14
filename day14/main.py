from collections import Counter, defaultdict

def load_data(src):
    with open(src,'r') as f:
        rules = {}
        template = None
        for line in f.readlines():
            line = line.strip()

            if not line:
                continue

            if not template:
                template = line
            else:
                first, second = line.split(' -> ')
                rules[first] = second

    return template, rules

# Naive way, doesn't work for part2
def part1(template, rules):
    new_polymer = template

    for _ in range(10):
        to_insert = []
        for i in range(len(new_polymer)):
            pair = new_polymer[i]+new_polymer[i+1] if i <= len(new_polymer)-2 else None
            
            if pair in rules:
                to_insert.append(rules[pair])
        
        to_insert.append('')
        new_polymer = ''.join(map(''.join, zip(new_polymer, to_insert)))

    stats = Counter(new_polymer)
    most_common = stats.most_common()[0][1]
    least_common = stats.most_common()[-1][1]

    return most_common - least_common

def part2(template, rules):
    pairs = defaultdict(int)
    for a,b in zip(template, template[1:]):
        pairs[a+b] += 1

    chars = defaultdict(int)
    for a in template: chars[a] += 1

    for _ in range(40):
        for (a,b), c in pairs.copy().items():
            x = rules[a+b]
            pairs[a+b] -= c
            pairs[a+x] += c
            pairs[x+b] += c
            chars[x] += c

    return max(chars.values()) - min(chars.values())


if __name__ == '__main__':
    template, rules = load_data('data.txt')
    result = part2(template, rules)
    print(result)
    