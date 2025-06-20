def selection_sort(arr):
    n = len(arr)
    for numIndex in range(n - 1):
        minIndex = numIndex
        for nextIndex in range(numIndex + 1, n - 1):
            if arr[nextIndex] < arr[minIndex]:
                minIndex = nextIndex

        # if minIndex != numIndex:
        temp = arr[numIndex]
        arr[numIndex] = arr[minIndex]
        arr[minIndex] = temp
    
    return arr


numberArray = [1, 73, 24, 16, 56, 3, 57, 63, 72, 29]
print(selection_sort(numberArray))
