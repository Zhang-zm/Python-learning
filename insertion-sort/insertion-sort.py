def insertionSort(arr):
    for i in range(1,len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0:
            if arr[j] > x:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = x
                break
            j = j - 1

        if j < 0:
            arr[0] = x

    return arr




t_arr = [3,5,6,8,12,13,2,1,4,7,9,15,14,16,10,20,11,18,17,19]

print(t_arr) # [3, 5, 6, 8, 12, 13, 2, 1, 4, 7, 9, 15, 14, 16, 10, 20, 11, 18, 17, 19]
print(insertionSort(t_arr)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
