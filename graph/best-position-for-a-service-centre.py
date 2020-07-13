from typing import List


class Solution:
    def disSum(self, x, y, pos):
        dis_sum = 0
        N = len(pos)
        for i in range(N):
            dis_x = abs(pos[i][0] - x)
            dis_y = abs(pos[i][1] - y)
            dis_sum += pow((dis_x * dis_x + dis_y * dis_y), 0.5)
        return dis_sum

    def getMinDistSum(self, positions: List[List[int]]) -> float:
        x, y = 0, 0
        N = len(positions)
        for p in positions:
            x += p[0]
            y += p[1]
        x /= N
        y /= N

        min_dis = self.disSum(x, y, positions)

        k = 0
        while k < N:
            for i in range(N):
                if i == k:
                    break
                xx, yy = positions[i][0], positions[i][1]
                dd = self.disSum(xx, yy, positions)
                if dd < min_dis:
                    min_dis = dd
                    x, y = xx, yy
            k += 1

        test_dis = 1000
        test_p = [[-1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, -1.0]]
        while test_dis > 10 ** -5:
            flag = 0
            for i in range(4):
                xx = x + test_dis * test_p[i][0]
                yy = y + test_dis * test_p[i][1]
                dd = self.disSum(xx, yy, positions)
                if dd < min_dis:
                    min_dis = dd
                    x, y = xx, yy
                    flag = 1
                    break
            if flag == 0:
                test_dis /= 2
        return min_dis


sol = Solution()
print(sol.getMinDistSum([[1, 1], [3, 3]]))
