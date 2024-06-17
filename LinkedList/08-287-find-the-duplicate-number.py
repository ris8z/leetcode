ex = 'https://leetcode.com/problems/find-the-duplicate-number/description/'

#really cool problem maybe dive deep into the math dimonstartion

"""
key points to get:
    index are important (sporatto quando hai un array con elementi da uno a n e lungo n)
        pk essenzialmente sia gli indici che i valori sono uguali
    
    con le determinate condizioni un array lo puoi vedere come una linked list
    floyd tells you if there is a cyrcle and can tell you where is its start

    you need to think different some times
    usando il fatto degli indici e il fatto che so sortati puoi invetarti una binaryserach shokkante
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyd algo O(n)
        def fun1(arr):
            # [1,3,4,2,2]
            #  0 1 2 3 4
            #key concept we check the index
            #our node is going to be something like
            #struct Node{
            #   val: idx
            #   next: nums[idx]
            #}
            #and two nodes are equal if their
            #values are equal

            #now you can just apply floyd as it is a normal liked list
            #the probelm is basically asking which node is the start of the cycle in this ll
            #and floyd alog answer just that question
            slow = fast = 0
            while True:
                slow = arr[slow]
                fast = arr[arr[fast]]
                if slow == fast: #il check sta dopo perche al inizio so uguali e si deve dare al tempo al fast di farsi tutto il giro e poi riacchiapre il lento sehhh let'sgoooo
                    break

            #we first find the point were slow and fast met
            #that is going always to exist bc we now that the list
            #contain n - 1 number, but as n spaces, so one value is going to be repated
            #and each node in the list point to another node in the list no one points to null

            #now floyd said to us that the distance from the start of the linked list and the met point
            #is equal so we can find the start of the cylce just by incrementing the two pointer one by one

            #How the math work?
            #speed = space / time
            #speed = how many nodes / one iteration
            #slow = 1 / 1 = 1
            #fast = 2 / 1 = 2
            #2 * slow = fast
            #let p be the part before the starting of the cylce
            #let x be the remaing part from the met point to the start of the cylce
            #let c be the length of the cylce
            #the slow point is going to end exactly on P + C - X
            #2 * (P + C - X) = (wherever the fast lands)

            #to catch the slow pointer the fast pointer need to trasverse the whole cyrcle so basically
            #2 * (P + C - X) = (P + C - X + C)
            #if you do the math you get
            #P = X

            #so the distance between the start of the ll and the start of the cylce
            #is going to be equal to the distance between the met point and the start of the cyle

            slow2 = 0
            while True:
                if slow2 == slow: #check prima caso mai lo start e' esattamente sulla testa
                    break
                slow2 = arr[slow2]
                slow = arr[slow]
            return slow

        #return fun1(nums)

        #binarysearch approch O(n*logn)
        def fun2(arr):
            # [1,3,4,2,2]
            #  0 1 2 3 4
            #the key point are always the indexs
            #we use the fact that they are the same number of the value in the array
            #and the fact that they are already sorted
            #for each mid that we got we want to ask
            #how many values are less or equal then this mid?
            #if the answer is less then the number itself it meas that it is not our man
            #and nither all the number before
            #ex if we got mid 2 and we count just two number less or equal they have to be just 1 and 2
            #so two it's not repaeted, and niether 1 becuse other ways the number smaller or equal than 2
            #should be 3
            #in the other case if the count is greater then mid our man is either the number itself or some
            #number before
            #this logic is pretty much all that we need to implement a good binarysearch

            left, right = 1, len(arr) - 1 # we start at 1 bc we don't care about 0 (problem guidelines)

            while left < right:
                mid = (left + right) // 2
                cnt = 0
                for n in arr:
                    if n <= mid:
                        cnt += 1
                if cnt > mid:
                    right = mid
                else:
                    left = mid + 1
            return left
        #return fun2(nums)
