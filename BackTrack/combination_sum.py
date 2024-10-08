from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        buffer: List[int] = []
        cnt: int = 0

        #O(k * C_r_{n,k})
        #C_r is combination without ripetation = n + k - 1 choose k
        #where k is target/min_in_candidates
        def dfs(i:int) -> None:
            nonlocal cnt
            if cnt == target:
                result.append(buffer.copy())
                return
            
            if cnt > target:
                return

            for j in range(i, len(candidates)):
                n = candidates[j]

                #branch with n
                buffer.append(n)
                cnt += n
                dfs(j)

                #remove n for the next branch
                buffer.pop()
                cnt -= n

        #O(2^(target/min) * target/min)
        def dfs_less_quick(i:int) -> None:
            nonlocal cnt
            if cnt == target:
                result.append(buffer.copy())
                return
            
            if i>= len(candidates) or cnt > target:
                return
            
            num = candidates[i]
            buffer.append(num)
            cnt += num
            dfs_less_quick(i)

            buffer.pop()
            cnt -= num
            dfs_less_quick(i+1)


        #dfs(0)
        dfs_less_quick(0)
        return result
