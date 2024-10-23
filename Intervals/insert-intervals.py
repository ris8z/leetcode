from typing import List
from math import ceil

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    start = 0
    end = 1
    if intervals == []:
        return [newInterval]
    
    res = []
    flag = True
    for i, currentInterval in enumerate(intervals):
        #print(f'new{newInterval}, curr={currentInterval}')

        #new start after the current end
        if newInterval[start] > currentInterval[end]:
            res.append(currentInterval)
            continue

        #new ends before the current start
        if newInterval[end] < currentInterval[start]:
            res.append(newInterval)
            res += intervals[i:]
            flag = False
            break

        #Here they are going to overlap for sure

        #curr is a subset of new
        if newInterval[start] <= currentInterval[start] and currentInterval[end] <= newInterval[end]:
            continue

        if currentInterval[start] <= newInterval[start]: 
            #currentInterval[start] <= newInterval[start] and newInterval[start] <= currentInterval[end]:
            newInterval[start] = currentInterval[start]
            newInterval[end] = max(newInterval[end], currentInterval[end])
        else:
            #currentInterval[start] <= newInterval[end] and newInterval[end] <= currentInterval[end]:
            newInterval[start] = min(newInterval[start], currentInterval[start])
            newInterval[end] = currentInterval[end]

    if flag:
        res.append(newInterval)

    return res 

    
intervals = [[-8,-6],[1,3], [6,5]]
newInterval = [-5,2]
output = [[-8,-6],[-5,3], [6,5]]
print(insert(intervals, newInterval) == output)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]
print(insert(intervals, newInterval) == output)

intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
print(insert(intervals, newInterval) == output)
