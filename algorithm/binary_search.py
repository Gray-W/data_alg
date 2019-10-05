

def binary_search(alist, item):
    """二分查找(递归版本)"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_2(alist, item):
    """二分查找，非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [14, 24, 35, 42, 56, 67, 72, 82, 94]
    print(binary_search(li, 67))
    print(binary_search(li, 100))
    print('---------2-------------')
    print(binary_search_2(li, 67))
    print(binary_search_2(li, 100))
