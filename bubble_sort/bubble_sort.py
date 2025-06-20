def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for loop in range(n):
        for i in range(0, n - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp
    return unsorted_list

# run
numberArray = [11, 7, 32, 21, 45, 4, 47, 63, 52, 29]
print(bubble_sort(numberArray))
