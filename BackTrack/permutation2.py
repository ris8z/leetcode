from typing import List, Dict

#we u hear unique first two thins that u need to think of are
#dict or sorting skipping

def permuteUnique(nums: List[int]) -> List[List[int]]:
    N:int = len(nums)
    result: List[List[int]] = []
    buffer: List[int] = []


    #nums.sort()
    visited: List[bool] = [False] * N
    def dfs():
        if len(buffer) == N:
            result.append(buffer.copy())
            return

        idx = 0
        while idx < len(nums):
            if visited[idx] is True:
                idx += 1
                continue
            
            element = nums[idx]
            
            visited[idx] = True
            buffer.append(element)
            dfs()

            visited[idx] = False
            buffer.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            idx += 1

    counter: Dict[int,int] = {}
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    print(counter)
    def with_map():
        if len(buffer) == N:
            result.append(buffer.copy())
            return
        
        for n in counter:
            if counter[n] > 0:
                buffer.append(n)
                counter[n] -= 1
                with_map()

                buffer.pop()
                counter[n] += 1

    #dfs()
    with_map()
    return result






nums = [1,1,2]
output = [[1,1,2],[1,2,1],[2,1,1]]
print(permuteUnique(nums))


