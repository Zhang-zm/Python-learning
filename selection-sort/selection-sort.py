def findSmallestFromArr(arr):
    smallest_item = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    result = []

    for i in range(len(arr)):
        smallestIndex = findSmallestFromArr(arr)
        result.append(arr.pop(smallestIndex))

    return result


print(selectionSort([1,2,5,1,10,-2,6])) # [-2,1,1,2,5,6,10]
