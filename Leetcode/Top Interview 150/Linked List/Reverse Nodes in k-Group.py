# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)  # dummy -> head
        grpPrev = dummy  # node before cur grp

        while True:
            kth = self.getKth(grpPrev, k)  # last node in cur grp
            # print(kth.val)
            if not kth:
                break
            grpNext = kth.next  # node after cur grp

            # reverse grp
            prev, curr = kth.next, grpPrev.next

            while curr != grpNext:  # loop cur grp
                tmp = curr.next
                # swap curr->prev = prev->curr
                curr.next = prev
                prev = curr
                curr = tmp  # curr = curr.next = prev

            tmp = grpPrev.next  # First node in cur grp
            grpPrev.next = kth  # update prev to end of this grp
            grpPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


l1 = tmp = ListNode(1)
inp = [2, 3, 4, 5]
for i in inp:
    tmp.next = ListNode(i)
    tmp = tmp.next

s = Solution()

l2 = s.reverseKGroup(l1, 2)
while l2:
    print(l2.val)
    l2 = l2.next
