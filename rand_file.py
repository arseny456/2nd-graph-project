from collections import deque

maze = {}

maze['a'] = ['b' , 'c']
maze['b'] = ['d', 'e']
maze['e'] = ['f']
maze['c'] = []
maze['d'] = []
maze['f'] = ['finish']

parents = {}
parents['c'] = 'a'
parents['b'] = 'a'

def search_finish(finish):
    search_queue = deque()
    search_queue += maze['a']
    searched = []

    while search_queue:
        node = search_queue.popleft()
        if not node in searched:
            try:
                if maze[node] == ['finish']:
                    print(node, 'is a finish node')
                    return True
                else:
                    search_queue += maze[node]
                    searched.append(node)
                    for key in maze[node]:
                        parents[key] = node
            except:
                pass
    return False

def search_path(f, start):
    way_list = [f]
    while f != start:
        f = parents[f]
        way_list.append(f)
    way_list.reverse()
    return way_list

if search_finish("a"):
    print(parents)
    print('The way is' , search_path('f', 'a'))
else:
    print('НЕТ ВЫХОДА')




