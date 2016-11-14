# Data is from CS Course from Stanford University
# This is the second homework
# Implementaiton of Merge Sort 
# Using Merge Sort to calculate number of inversions in a list

dataList = []
f = open("IntegerArray.txt")
for line in f:
    line = line.rstrip()
    line = int(line)
    dataList.append(line)
f.close()

def mergeSort(aList, s, e):
    size = len(aList)
    temp = [0] * size
    return _mergeSort(aList, temp, s, e)

def _mergeSort(aList, helper,s, e):
    if s < e:
        mid = (s + e - 1) // 2
        a = _mergeSort(aList, helper, s, mid)
        b = _mergeSort(aList, helper, mid + 1, e)
        c = merge(aList, helper, s, mid, e)
        return a + b + c
    return 0

def merge(li, helper, begin, middle, end):  
    for i in range(begin, end + 1):
        helper[i] = li[i]
    leftRun = begin
    rightRun = middle + 1
    runnerIndex = begin
    inversions = 0

    while leftRun <= middle and rightRun <= end:
        if helper[leftRun] < helper[rightRun]:
            li[runnerIndex] = helper[leftRun]
            leftRun += 1
        else:
            li[runnerIndex] = helper[rightRun]
            rightRun += 1
            inversions += middle + 1 - leftRun
        runnerIndex += 1
    
    while leftRun <= middle:
        li[runnerIndex] = helper[leftRun]
        leftRun += 1
        runnerIndex += 1
    
    while rightRun <= end:
        li[runnerIndex] = helper[rightRun]
        rightRun += 1
        runnerIndex += 1
    return inversions
    
c = mergeSort(dataList, 0, len(dataList) - 1)
print(c)


# Code written by Riley Du
# Github: https://github.com/rileydu24