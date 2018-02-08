import math

def formatLog(arr):
    f_number_MAX = int(math.ceil(math.log(len(arr),2))) # 树的高度

    for f_number in range(1,f_number_MAX+1):
        nodes_len = int(math.pow(2, f_number -1))
        start_i = int(math.pow(2,f_number - 1) -1)
        row_arr = arr[start_i:(start_i + nodes_len)]

        print(row_arr)

formatLog([1,2,4,5,6,77])
