def sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_arr = sort(arr[:mid])
    right_arr = sort(arr[mid:len(arr)])

    tmp_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr):
        if left_arr[l] < right_arr[h]:
            tmp_arr.append(left_arr[l])
            l += 1
        else:
            tmp_arr.append(right_arr[h])
            h += 1
    tmp_arr += left_arr[l:]
    tmp_arr += right_arr[h:]


arr = [2, 7, 3, 4, 9, 5]
sort(arr)
