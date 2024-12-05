from collections import deque


def min_steps_to_corners(start):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    corners = [(0, 0), (0, 3), (3, 0), (3, 3)]
    visited = set()
    queue = deque([(start, 0)])  # (position, steps)

    while queue:
        (x, y), steps = queue.popleft()

        # 如果到达任意一个角落
        if (x, y) in corners:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1  # 如果无法到达


# 示例用法
start_position = (1, 1)  # 从中心开始
steps = min_steps_to_corners(start_position)
print(f"从{start_position}到达四个顶点的最少步数: {steps}")
