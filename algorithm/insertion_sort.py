def insertion_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的操作
    for j in range(1, n):  # 1~n-1
        # j 代表内层循环起始值
        # 执行从右边的无序序列中取出第一个元素，即j位置的元素，然后将其插入到前面的正确位置中
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j -= 1
            else:
                break


if __name__ == '__main__':

    alist = [12,42,53,23,56,34,6,34]
    insertion_sort(alist)
    print(alist)