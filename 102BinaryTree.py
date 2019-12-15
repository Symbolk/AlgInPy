from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def build_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        length = len(values)
        nums = 1
        while nums < length:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < length:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1


def build_tree(arr):
    node_list = []
    for i in range(len(arr)):
        node = TreeNode(arr[i])
        node_list.append(node)
    if len(node_list) > 0:
        for i in range(int(len(arr) / 2) - 1):
            if node_list[2 * i + 1].left is None:
                node_list[i].left = node_list[2 * i + 1]
            if node_list[2 * i + 2].right is None:
                node_list[i].right = node_list[2 * i + 2]
        last_idx = int(len(arr) / 2) - 1
        node_list[last_idx].left = node_list[last_idx * 2 + 1]
        if len(arr) % 2 == 1:
            node_list[last_idx].right = node_list[last_idx * 2 + 2]
    return node_list


arr = [3, 9, 20, None, None, 15, 7]
node_list = build_tree(arr)


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res = []
    cur_level = [root]
    while cur_level:
        tmp = []
        next_level = []
        for node in cur_level:
            tmp.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res.append(tmp)
        cur_level = next_level
    return res


print(levelOrder(node_list[0]))

tree = Tree()
tree.build_tree(arr)
print(levelOrder(tree.root))
