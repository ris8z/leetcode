ex: str = 'https://leetcode.com/problems/reverse-linked-list/description/'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #---------
        #recursive
        #---------
        def fun1(prev, curr):
            if not curr:
                return prev
            link = curr.next
            curr.next = prev
            return fun1(curr, link)
        #return fun1(None, head)

        def fun2(prev, curr):
            if not curr:
                return prev
            newHead = fun(curr, curr.next)
            curr.next = prev
            return newHead
        #return fun2(None, head)

        def fun3(node):
            if not node or not node.next:
                return node
            newHead = fun(node.next)
            node.next.next = node
            node.next = None
            return newHead
        #return fun3(head)

        #---------
        #iterative
        #---------

        def fun4(h):
            prev = None
            curr = h
            while curr:
                link = curr.next
                curr.next = prev
                prev, curr = curr, link
            return prev
        #return fun4(head)
