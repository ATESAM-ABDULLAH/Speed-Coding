# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = res = ListNode(0)  # New Linked List
        carry = 0

        while l1 or l2 or carry:  # if int leftover
            v1 = v2 = 0  # Store values from each linked list
            if l1:  # if node left in l1
                v1 = l1.val
                l1 = l1.next
            if l2:  # if node left in l2
                v2 = l2.val
                l2 = l2.next
            res.next = ListNode(((v1 + v2 + carry) % 10))
            carry = (v1 + v2 + carry) // 10
            print(f"{v1}+{v2}={res.val}->{carry}")
            res = res.next
        return head.next


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
l2.next.next.next.next = ListNode(9)

s = Solution()
res = s.addTwoNumbers(l1, l2)

while res != None:
    print(res.val, end=" ")
    res = res.next
