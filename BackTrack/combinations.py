from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        buffer: List[int] = []
        lenght: int = n

        #O(k * (2 ^ n))   k is for copying
        def dfs(i: int) -> None:
            if len(buffer) == k:
                result.append(buffer.copy())
                return
            
            if i >= lenght:
                return
            
            num = i + 1
            #branch with num
            buffer.append(num)
            dfs(i + 1)

            #branch without num
            buffer.pop()
            dfs(i + 1)
        
        #O(k * C_{n,k})
        def better_dfs(i: int) -> None:
            if len(buffer) == k:
                result.append(buffer.copy())
                return
            
            if i >= lenght:
                return
            
            for j in range(i,lenght):
                nums = j + 1
                buffer.append(nums)
                better_dfs(j + 1)
                buffer.pop()
        #dfs(0)
        better_dfs(0)
        return result
