

def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left/right 归并排序后的有序的新的列表
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的整体
    # merge left right
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [54, 28, 98, 17, 38, 49, 82, 20]
    print(li)
    sorted_list = merge_sort(li)
    print(sorted_list)
