from typing import List

def dis(nums: List[int], k: int) -> List[List[int]]:
    result: List[List[int]] = []
    buffer: List[int] = []
    visited: List[bool] = [False] * len(nums)

    def dfs():
        if len(buffer) == k:
            result.append(buffer.copy())
            return

        for idx, val in enumerate(nums):
            if visited[idx]:
                continue

            buffer.append(val)
            visited[idx] = True
            dfs()

            buffer.pop()
            visited[idx] = False
    dfs()
    return result

nums = list(range(1,6))
k = 2
print(dis(nums,k))

