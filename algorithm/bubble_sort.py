

def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n-1):  # 0 ~ len-1
        count = 0
        for i in range(0, n-1-j):
            # 比较一遍
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        if count == 0:
            return


if __name__ == '__main__':
    li = [2, 4, 89, 23, 47, 58,98]
    print(li)
    bubble_sort(li)
    print(li)