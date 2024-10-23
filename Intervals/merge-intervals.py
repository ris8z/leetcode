from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    start: int = 0
    end: int = 1

    curr_start: int = -1 
    curr_end: int = -1 

    intervals = sorted(intervals, key=lambda x:x[start])

    result: List[List[int]] = []

    for interval in intervals:
        #first iteration
        if curr_start == -1:
            curr_start, curr_end = interval[start], interval[end]
            continue
        #no overlap
        if interval[start] > curr_end:
            result.append([curr_start, curr_end])
            curr_start, curr_end = interval[start], interval[end]
            continue
        #overlap
        curr_end = max(curr_end, interval[end]) 

    result.append([curr_start, curr_end])

    return result 
        





intervals = [[0,5], [7,12], [10,11]]
output = [[0,5], [7,12]]
print(merge(intervals) == output)


intervals = [[1,3],[2,6],[8,10],[15,18]]
output = [[1,6],[8,10],[15,18]]
print(merge(intervals) == output)


intervals = [[1,4],[4,5]]
output = [[1,5]]
print(merge(intervals) == output)
