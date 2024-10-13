from typing import List, Dict



def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    result: List[List[int]] = []
    buffer: List[int] = []
    cnt: int = 0

    candidates.sort()
    def dfs(i):
        nonlocal cnt
        if cnt == target:
            result.append(buffer.copy())
            return

        if cnt > target:
            return

        if i >= len(candidates):
            return

        n:int = candidates[i]

        buffer.append(n)
        cnt += n
        dfs(i + 1)

        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1

        buffer.pop()
        cnt -= n
        dfs(i + 1)

    dfs(0)
    return result





candidates = [10,1,2,7,6,1,5]
target = 8
output = [[1,1,6],[1,2,5],[1,7],[2,6]]
print(combinationSum2(candidates, target))
