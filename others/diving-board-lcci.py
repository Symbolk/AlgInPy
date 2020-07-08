class Solution:
    # brutal force: O(klogk), O(k)
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        length = set()
        for i in range(k + 1):
            j = k - i
            length.add(i * longer + j * shorter)
        res = list(length)
        res.sort()
        return res

    # O(k), O(1)
    def divingBoard1(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        # longer * i + shorter*(k-i) = (longer-shorter)*i + shorter * k
        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = (longer - shorter) * i + shorter * k
        return res

    def divingBoard2(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [shorter * k]
        diff = longer - shorter
        for i in range(1, k + 1):
            res.append(res[-1] + diff)
        return res
