from collections import deque

# 定义二叉树节点
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzag_level_order(root):
    if not root:
        return []

    result = []
    current_level = deque([root])
    left_to_right = True  # 标记当前层的遍历方向

    while current_level:
        level_size = len(current_level)
        level_values = []

        for _ in range(level_size):
            if left_to_right:
                node = current_level.popleft()
                level_values.append(node.value)
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
            else:
                node = current_level.pop()
                level_values.append(node.value)
                if node.right:
                    current_level.appendleft(node.right)
                if node.left:
                    current_level.appendleft(node.left)

        result.append(level_values)
        left_to_right = not left_to_right  # 切换方向

    return result


from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# 示例用法
if __name__ == "__main__":
    # 创建二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # 进行之字形遍历
    result = zigzag_level_order(root)
    print(result)  # 输出: [[1], [3, 2], [4, 5, 6, 7]]
    result = level_order(root)
    print(result)
