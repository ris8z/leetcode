ex = 'https://leetcode.com/problems/search-in-rotated-sorted-array/description/'

#ricodati fatti l'esempio con un array 1, 2, 3 tutte le possibilita di rotazione alla fine 3 so
# non ruotato
# ruotato di uno
# ruotato di due
#ez isi bisi lemon squzi

class Solution:
    def search(self, a: List[int], target: int) -> int:
        # left < mid -> (left - mid is sorted) (not rotated at all)
        # [1, 2, 3]
        #        /
        #     /
        #  /

        # left > mid -> (mid - right is sorted) (rotated of 1)
        # [3, 1, 2]
        #
        #        /
        #  /  /

        # left < m -> (left - mid is sorted) (rotated of 2)
        # [2, 3, 1]
        #
        #     /
        #  /     /


        #special case mid = left
        # mid = left -> (left - mid sorted)
        # [1, 1, 2]

        #grouping up the informations
        
        #if a[left] <= a[mid]:
            #from left to mid is sorted
        #else:
            #in the case a[left] > a[mid]
            #from mid to right is sorted

        #let's write the bs
        #we can easly say when guess = target so we use the approch with <=

        left, right = 0, len(a) - 1

        while left <= right:
            mid = left + (right - left) // 2 #to avoid overflow

            if a[mid] == target:
                #we got an hit
                return mid

            if a[left] <= a[mid]:
                #sorted (left - mid)
                if a[left] <= target and target < a[mid]:
                    #we know our target must be in the left part
                    right = mid - 1
                else:
                    #we know our target must be in the right part
                    left = mid + 1
            else:
                #sorted (mid - right)
                if a[mid] < target and target <= a[right]:
                    #we know our target must be in the right part
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

