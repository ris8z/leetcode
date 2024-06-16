"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #just for debug:
        def printList(node):
            if not node:
                return
            print(f'({node}),({node.val}),({node.random})')
            printList(node.next)


        #approach with dictonary
        def fun(head):
            #it's a dict where the key are the original node and the value the copy
            #we start with None to copy also the None node the last one
            oldToNew = {None:None}

            curr = head
            while curr:
                oldToNew[curr] = Node(curr.val)
                curr = curr.next

            #now we need to fill the value of next and random for the copied list
            curr = head
            while curr:
                copy = oldToNew[curr]
                copy.next = oldToNew[curr.next]
                copy.random = oldToNew[curr.random]
                curr = curr.next

            #the head of the copied linkedlist is going to be the one liked to the original
            return oldToNew[head]

        #return fun(head)


        #approach with no dictonay
        def fun1(head):
            #we need to create a copy of each node and insert it in the list between his orignal version
            #and the next node to copy

            curr = head
            while curr:
                new = Node(curr.val, curr.next, curr.random)
                curr.next = new
                curr = curr.next.next
            
            #we need to get the re wire the random pointer in the copied nodes
            #the right address is going to be the next after the one that theey are already pointing to
            curr = head
            while curr:
                copy = curr.next
                copy.random = copy.random.next if copy.random else None
                curr = curr.next.next

            #now we just need to split the two list
            original = head
            copy = head_copy = head.next
            while original:
                original.next = original.next.next
                copy.next = copy.next.next if copy.next else None
                original, copy = original.next, copy.next

            return head_copy

        return fun1(head)

