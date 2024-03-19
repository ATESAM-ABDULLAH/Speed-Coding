# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = tmp = ListNode(0)

        while list1 and list2:  # While both lists left
            if (list1.val <= list2.val) or (not list2):  # Add l1.val into l3
                # print("l1", list1.val)
                tmp.next = ListNode(list1.val)
                list1 = list1.next

            elif (list1.val > list2.val) or (not list1):  # Add l2.val into l3
                # print("l2", list2.val)
                tmp.next = ListNode(list2.val)
                list2 = list2.next

            tmp = tmp.next

        if list1:  # if list1 left
            tmp.next = list1
        if list2:  # if list2 left
            tmp.next = list2

        return res.next


l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)



s = Solution()
l3 = s.mergeTwoLists(l1, l2)

while l3 != None:
    print(l3.val, end=" ")
    l3 = l3.next
