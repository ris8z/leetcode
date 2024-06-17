# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#floyd algo
#check if there is a crycle
#start with two pointers one moving twice as fast as the first one
#if they met there is a circyle

#the distance from the start of the list and the met point between the slow and fast point is always the same
#so you can get the start of a cyrcle by adding another pointer slow2 pointing to the head
#and moving slow2 and slow2 1 stap each iteration
#they are going to met at the start of the
#cycle

#for more info and toughts check the find duplicate number solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast = head
        found = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break

        if not found:
            return None

        slow2 = head
        while True:
            if slow2 == slow:# checckiamo prima perche potrebbe essere che il primo punto e' la testa
                break
            slow2 = slow2.next
            slow = slow.next
        return slow
