ex:'https://leetcode.com/problems/koko-eating-bananas/description/'



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [12, 8, ..., 8, 8, 4] the values are the number of hours at k speed 
        # 1, 4, ..., 9 10 11 the indexs are k 
        # ovviamente la velocita minima e' procodio uno 
        #let m = max(piles) 
        #let n = len(piels) 
        #time compelxity O(nlog(m)) 
        #we want the min index in a bs so we use the version that don have 
        #the return statement in the while loop
        
        # 12, 8, 8, 8, 8, 4
        # 1   2  3  4  5  6
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            guess = 0
            for n in piles:
                guess += math.ceil(float(n) / mid)

            if guess > h:
                left = mid + 1
            else:
                right = mid

        return left
