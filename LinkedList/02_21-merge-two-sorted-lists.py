ex = 'https://leetcode.com/problems/merge-two-sorted-lists/description/'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #---------
        #recursive    
        #---------
        def fun1(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            small, big = (l1, l2) if l1.val < l2.val else (l2, l1)
            small.next = fun1(small.next, big)

            return small
        #return fun1(list1, list2)

        #---------
        #iterative
        #---------
        def fun2(l1, l2):
            dummy = curr = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 or l2

            return dummy.next
        #return fun2(list2, list2)
