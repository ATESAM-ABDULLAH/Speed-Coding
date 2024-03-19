# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        # Store vals in a list
        tmp1 = head
        vals = []
        while tmp1:
            vals.append(tmp1.val)
            tmp1 = tmp1.next

        if len(vals) == 1:
            return head

        # Reverse the needed part
        vals[left - 1 : right] = reversed(vals[left - 1 : right])

        # Now just change values as needed
        tmp2 = head
        count = 1
        while tmp2:
            tmp2.val = vals[count - 1]
            count += 1
            tmp2 = tmp2.next

        return head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)

s = Solution()
ret = s.reverseBetween(l1, 2, 4)
while ret:
    print(ret.val, end=" ")
    ret = ret.next
