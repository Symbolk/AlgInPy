from typing import List

# Geometric Median
# There isn’t any defined correct algorithm for finding the Geometric Median
# Here we are approximating a solution
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
        # current temp median (ans)
        x, y = 0, 0
        N = len(positions)
        for p in positions:
            x += p[0]
            y += p[1]
        # get the Centroid
        x /= N
        y /= N

        # current temp min distance sum
        min_dis = self.disSum(x, y, positions)

        # iterate over the given input points
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

        # learning rate/step
        step = 1000
        move = [[-1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, -1.0]]
        # terminate when lower_limit exceeds the test_distance
        while step > 10 ** -5:
            flag = 0
            for i in range(4):
                xx = x + step * move[i][0]
                yy = y + step * move[i][1]
                dd = self.disSum(xx, yy, positions)
                if dd < min_dis:
                    min_dis = dd
                    x, y = xx, yy
                    # find one then break to move from new (x,y)
                    flag = 1
                    break
            # else binary the step
            if flag == 0:
                step /= 2
        return min_dis


sol = Solution()
print(sol.getMinDistSum([[1, 1], [3, 3]]))
