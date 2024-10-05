from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        buffer: List[int] = []
        def dfs(idx: int) -> None:
            if idx >= len(nums):
                result.append(buffer.copy())
                return
            n = nums[idx]

            #branch with n
            buffer.append(n)
            dfs(idx + 1)

            #branch without n
            buffer.pop()
            dfs(idx + 1)
        
        dfs(0)
        return result
