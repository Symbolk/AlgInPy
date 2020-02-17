class Solution:
    def getIntersectionNode(self, headA, headB):
        i, j = headA, headB
        while i != j:
            i = i.next if i else headB
            j = j.next if j else headA
        return i
