from collections import deque

maze = {}

maze['1'] = ['2']
maze['2'] = ['3','5']
maze['3'] = []
maze['4'] = ['5']
maze['5'] = ['4','6','8']
maze['6'] = []
maze['7'] = ['8']
maze['8'] = ['9']
maze['9'] = ['finish']


parents = {}
parents['2'] = '1'


def search_finish(finish):
    search_queue = deque()
    search_queue += maze['1']
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

if search_finish("1"):
    print(parents)
    print('The way is' , search_path('f', '1'))
else:
    print('НЕТ ВЫХОДА')




