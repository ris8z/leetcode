ex = 'https://leetcode.com/problems/binary-search/'



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Utile quando stai cerando il minimo di un iniseme di numeri uguali
        #tipo koko e le banane
        #oppure quando non riusciamo a definire bene una condizione specifica
        #per cui la nostra guess e uguale alla query
        def fun1(a, q):
            #we just wanto to choose a number by make the two pointer equals and
            #then check if left is the index of the target
            #IMPORTANT if u have something like [1,2,2,2,2,3,4,5,6]
            #and you are seraching two you are going to get the first one
            #because we do not return in the while loop
            left, right = 0, len(a) - 1

            #due to the fact we dont return in the while loop
            #left must be just < than right without =
            while left < right:
                mid = left + (right - left) // 2#or just (left+right)//2
                if a[mid] < q:
                    left = mid + 1
                else:
                    right = mid #you can't get in a infinte loop bc // always round down the number
            if a[left] == q:
                return left
            return -1
        return fun1(nums, target)
        

        #Utile quando abbiamo un target prescisio che possiamo individure
        #as soon as we hit the q we return it
        #we can easly check if our guess is equal to the query
        #a bit more efficent than the other one
        #but you don't get each time the first two but one random
        #in this case left must be <= than right bc the return statemtn is
        #in the while loop
        def fun2(a, q):
            left, right = 0, len(a) - 1

            while left <= right:
                mid = left + (right - left) // 2
                # left + right // 2 - left // 2
                # left // 2  + right // 2
                # (left + right) // 2 this one can lead to overflow
                # so you to the - first

                if a[mid] == q:
                    return mid

                if a[mid] < q:
                    left = mid + 1
                else:
                    #a[mid] > q
                    right = mid - 1
            return -1
        return fun2(nums, target)
