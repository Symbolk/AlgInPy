import random

# 定义马的位置
start_position = (1, 1)  # 从中心开始
vertices = [(0, 0), (0, 3), (3, 0), (3, 3)]
visited = set()
visited.add(start_position)

# 定义马的移动方式
def get_possible_moves(position):
    x, y = position
    moves = []
    if x > 0: moves.append((x - 1, y))  # 上
    if x < 3: moves.append((x + 1, y))  # 下
    if y > 0: moves.append((x, y - 1))  # 左
    if y < 3: moves.append((x, y + 1))  # 右
    return moves

# 模拟随机过程
steps = 0
current_position = start_position

while len(visited) < 5:  # 需要包含四个顶点和起始点
    possible_moves = get_possible_moves(current_position)
    current_position = random.choice(possible_moves)
    visited.add(current_position)
    steps += 1

print(f"总共跳了 {steps} 步，访问的位置包括: {visited}")
