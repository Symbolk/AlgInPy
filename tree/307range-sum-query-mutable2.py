class SegmentTree:
    def __init__(self, data, merge):
        '''
        :param data: raw array
        :param merge: how to merge child nodes (sum? max? min?)
        '''
        self.data = data
        self.size = len(data)
        self.tree = [None] * (4 * self.size)
        self._merge = merge
        if self.size:
            self._build(0, 0, self.size - 1)

    def query(self, ql, qr):
        return self._query(0, 0, self.size - 1, ql, qr)

    def update(self, index, value):
        self.data[index] = value
        self._update(0, 0, self.size - 1, index)

    def _build(self, tree_index, l, r):
        '''
        :param index: index of the node in the data array
        :param l: the left border of the range of node
        :param r: the right border of the range
        :return:
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = l + ((r - l) >> 1)
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        self._build(left, l, mid)
        self._build(right, mid + 1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])

    def _query(self, tree_index, l, r, ql, qr):
        '''
        :param tree_index: index of a non-left node
        :param l: the left
        :param r: and right border of the range
        :param ql: the left
        :param qr: and right border of the query
        :return:
        '''
        if l == ql and r == qr:
            return self.tree[tree_index]
        mid = l + ((r - l) >> 1)
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # in left child
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # in right child
            return self._query(right, mid + 1, r, ql, qr)
        # part in left and right
        return self._merge(self._query(left, l, mid, ql, mid), self._query(right, mid + 1, r, mid + 1, qr))

    def _update(self, tree_index, l, r, index):
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = l + ((r - l) >> 1)
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            self._update(right, mid + 1, r, index)
        else:
            self._update(left, l, mid, index)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])


class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums, lambda x, y: x + y)

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)
