def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        # mid = int((low + high) / 2)  # python3 "/"所得为float 作为列表索引需取整，或者用"//"向下取整
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


t_list = [1,2,4,6,8,10,12]
t_item = 0
print(binary_search(t_list,t_item)) # None
print(binary_search(t_list,6)) # 3
