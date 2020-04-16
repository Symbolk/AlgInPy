# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        s = []
        j = 0
        for i in range(len(pushV)):
            s.append(pushV[i])
            while s and j < len(popV) and s[-1] == popV[j]:
                s.pop()
                j += 1
        return not s
