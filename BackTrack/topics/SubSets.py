from typing import List

# recursive O(n * (2 ** n) without the time for mybuffer.copy()
def subsets(arr: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    mybuffer: List[int] = []

    def dfs(idx: int) -> None:
        if idx >= len(arr):
            result.append(mybuffer.copy())
            return

        mybuffer.append(arr[idx])
        dfs(idx + 1)

        mybuffer.pop()
        dfs(idx + 1)

    dfs(0)
    return result

# itrative O(n * (2 ** n) without the time for the copy of sb +[n]
def subsets_iterative(arr: List[int]) -> List[List[int]]:
    subsets: List[List[int]] = [[]]

    for n in arr:
        new_subsets: List[List[int]] = []
        for sb in subsets:
            new_subsets.append(sb + [n])
        subsets.extend(new_subsets)

    return subsets


print(subsets([1,2,3]))
print(subsets_iterative([1,2,3]))

