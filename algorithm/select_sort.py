
alist = [12,42,53,23,56,34,6,34]

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(0, n-1):  # 0 ~ n-2  1 ~ n-1
        min_index = j
        for i in range(j+1, n):  # j+1 ~ n-1
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

select_sort(alist)
print(alist)