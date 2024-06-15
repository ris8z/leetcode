ex = 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/'



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #All these approches use the dummy node trick :)

        #recursive: 
        
        #(one return type)
        #the idea is to go down to the end of the list with rec, and re wireing the list
        #but when we are in the right spot we just pass the link for the next node
        def rec1(node):
            if not node:
                return None
            node.next = rec1(node.next)
            rec1.pos += 1

            if rec1.pos == n:
                #we are in the target node so we want to return the one after this
                return node.next
            
            #we are in some others node so we just return node'
            return node
        
        #we start at 0 so in n step you get to the target node
        rec1.pos = 0
        return rec1(ListHead(0, head)).next

        
        #(two different return type) (don't need to use a static var or a global var)
        #the idea is the same but we want to stay one before the target to get rid of it
        #so we start at -1 (in the sense that the none at the end of list is -1 one and then
        #going up we add n times 1 and when we get to n we are one beofre the target node
        def rec2(node):
            if not node:
                None, -1

            _, pos = rec2(node.next)
            pos += 1

            if pos == n:
                node.next = node.next.next

            return node, pos

        return rec2(ListHead(0, head))[0].next

        #I think you can take the best from these two function and get a third one we the idea of the
        #first one and the double value so (no static var) of the second one
        #actully let's try
        #just bc i think that if we need to handle the fact that we need to stay before the target
        #it's better go for an itertive approach

        def rec3(node):
            if not node:
                None, 0

            node.next, pos = rec3(node.next)
            pos += 1

            if pos == n:
                return node.next, pos

            return node, pos

        
        return rec3(ListHead(0, head))[0].next

        
        #iterative (last approach)

        def itr(head, n):
            # d 1 2 3 n     2
            # s
            # f

            # s   f

            #  s    f
            #     s   f
            #se famo finire fast a none slow sta esattamente sul target
            #essendo un sll conviene stare prime qundi famo finire fast a quello prima di null
            
            #il trick e' che se hai due nodi di distanza bho 2 se trasli i due nodi uno a uno
            #finqunado qullo piu avanti tocca per primo la fine quei due nodi avranno sempre due di distanza
            #e quindi starai al numero numero due dalla fine (tecincamente il 3 in realta)
            Dummy = ListNode(0, head)

            slow = fast = dummy
            while fast and n > 0:
                fast = fast.next
                n -= 1
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next

            slow.next = slow.next.next

            return dummy.next

        return itr(head, n)
