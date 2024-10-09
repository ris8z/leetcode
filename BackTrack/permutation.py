from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    buffer: List[int] = []
    N = len(nums)
    visited: List[bool] = [False] * N 
    
    def dfs():
        if len(buffer) == N:
            result.append(buffer.copy())
            return
        
        for idx, element in enumerate(nums):
            if visited[idx]:
                continue

            visited[idx] = True
            buffer.append(element)
            dfs()

            visited[idx] = False
            buffer.pop()

    dfs()
    print(result)
         
    return []


nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute(nums))
