from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        buffer: List[int] = []
        nums.sort()
        
        def dfs(i: int) -> None:
            if i >= len(nums):
                result.append(buffer.copy())
                return
            
            #branch with all the subsets with at least one n
            buffer.append(nums[i])
            dfs(i + 1)

            #branch with all the subsets with NO ONE n
            buffer.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result
