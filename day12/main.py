from collections import defaultdict

def load_data(src):
    with open(src,'r') as f:
        graph = defaultdict(list)
        for line in f.readlines(): 
            a, b = line.strip().split('-')
            graph[a].append(b)
            graph[b].append(a)
        return graph

def part2(graph):
    queue = [['start']]
    finished = 0
    full_paths = []

    while queue:
        path = queue.pop(0)

        #iterate over adjacent nodes
        for current_node in graph[path[-1]]:
            is_repeat = current_node.islower() and current_node in path

            if current_node == 'end':
                finished += 1
                path.append('end')
                full_paths.append(path)
                
            elif current_node != 'start' and not (path[0] == '*' and is_repeat):
                queue.append((['*'] if is_repeat else []) + path + [current_node])
		


    return finished
    

if __name__ == '__main__':
    data = load_data('data.txt')
    result = part2(data)
    print(result)

	

