
from typing import List

# Time: O(k * 2^n)
def comb(nums: List[int], k: int) -> List[List[int]]:
    result: List[List[int]] = []
    buffer: List[int] = []
    def dfs(i: int) -> None:
        if len(buffer) == k:
            result.append(buffer.copy())
            return

        if i >= len(nums):
            return
        
        n: int = nums[i]
        #all the combination with n
        buffer.append(n)
        dfs(i + 1)

        #all the combination without n
        buffer.pop()
        dfs(i + 1)

    dfs(0)
    return result

# O(k * C(n,k))
def improved(nums: List[int], k:int) -> List[List[int]]:
    result: List[List[int]] = []
    buffer: List[int] = []
    def dfs(i: int) -> None:
        if len(buffer) == k:
            result.append(buffer.copy())
            return
        
        if i >= len(nums):
            return


        for j in range(i, len(nums)):
            n: int = nums[j]
            buffer.append(n)
            dfs(j + 1)
            buffer.pop()

    dfs(0)
    return result


nums = list(range(1,6))
k = 2
print(nums, k)

print(comb(nums,k))
print(improved(nums,k))
