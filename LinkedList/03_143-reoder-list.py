ex = 'https://leetcode.com/problems/reorder-list/description/'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            if not node or not node.next:
                return node
            newhead = reverse(node.next)
            node.next.next = node
            node.next = None
            return newhead

        def merge(l1, l2):
            while l2:#we know that l2 is shorter than l1
                link1, link2 = l1.next, l2.next
                l1.next = l2
                l2.next = link1
                l1, l2 = link1, link2

        #find the middle point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #cut the list into the middle point to create two list left and right
        #left is going to be greater than right bc left is going to be n/2 + 1 elements
        leftList = head
        rightList = slow.next # it starts at the element after the middle one
        slow.next = None # the actual cut

        #reverse the right list
        rightList = reverse(rightList)

        #merge them (rember that leftList is smaller than rightList)
        merge(leftList, rightList)
