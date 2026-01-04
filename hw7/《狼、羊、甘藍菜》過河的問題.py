# 狀態: (man, wolf, goat, cabbage)
# 0 = left bank, 1 = right bank

from collections import deque

def is_safe(state):
    m, w, g, c = state
    # 狼吃羊
    if w == g and m != w:
        return False
    # 羊吃菜
    if g == c and m != g:
        return False
    return True

def next_states(state):
    m, w, g, c = state
    moves = []
    # 人單獨過河
    moves.append((1-m, w, g, c))
    # 人帶狼
    if m == w:
        moves.append((1-m, 1-w, g, c))
    # 人帶羊
    if m == g:
        moves.append((1-m, w, 1-g, c))
    # 人帶菜
    if m == c:
        moves.append((1-m, w, g, 1-c))
    return moves

def solve():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for ns in next_states(state):
            if ns not in visited and is_safe(ns):
                visited.add(ns)
                queue.append((ns, path + [ns]))

solution = solve()
for step in solution:
    print(step)
