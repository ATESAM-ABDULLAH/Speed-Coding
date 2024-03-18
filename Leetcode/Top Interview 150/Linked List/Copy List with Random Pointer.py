# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Interleave val only: 1->1'->2->2' ...
        tmp1 = head
        while tmp1 != None:
            newNode = Node(tmp1.val + 1, None, None)  # new Node with val only
            # Place node: tmp1 -> newNode -> tmp1.next
            newNode.next = tmp1.next
            tmp1.next = newNode
            tmp1 = newNode.next

        # Connect Random ptrs
        tmp2 = head
        flag = 1  # 1 = oldNode, 0 = newNode
        while tmp2 != None:
            # newrand = oldrand.next
            if flag == 1:  # oldNode: store rand ptr
                oldrand = tmp2.random
            else:  # newNode: set rand ptr to newrand
                tmp2.random = oldrand.next if oldrand else None
            # print(tmp2.val, (tmp2.random.val if tmp2.random else None))
            flag = not flag  # switch flag
            tmp2 = tmp2.next

        # Seperate into orig,copy lists
        tmp4 = head
        copy = c_tmp = head.next
        while c_tmp.next != None:
            tmp4.next = tmp4.next.next  # Orig List: skip 1
            tmp4 = tmp4.next

            c_tmp.next = c_tmp.next.next  # Copy List: skip 1
            c_tmp = c_tmp.next
        tmp4.next = tmp4.next.next
        return copy, head


# input = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = Node(7, None, None)
head.next = Node(13, None, None)
head.next.next = Node(11, None, None)
head.next.next.next = Node(10, None, None)
head.next.next.next.next = Node(1, None, None)

head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

s = Solution()

ret, newhead = s.copyRandomList(head)

while newhead:
    print("h", newhead.val, (newhead.random.val if newhead.random else None))
    newhead = newhead.next
print("\n\n")
while ret:
    print("r", ret.val, (ret.random.val if ret.random else None))
    ret = ret.next
