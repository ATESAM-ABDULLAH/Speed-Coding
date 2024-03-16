# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: # <2 items
            return False
        slow = fast = head # ptr start at head
        while (fast != None) and (fast.next != None): # if end not reached
            slow = slow.next # slow +=1
            fast = fast.next.next # fast +=2
            if slow == fast:  # loop: fast looped behind slow
                return True
        return False


h = ListNode(3)
h.next = ListNode(2)
h.next.next = ListNode(0)
h.next.next.next = ListNode(-4)
h.next.next.next.next = h.next.next.next

s = Solution()
print(s.hasCycle(h))
