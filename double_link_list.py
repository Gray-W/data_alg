from single_link_list import SingleLinkList


class Node(object):
    """结点"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):
    """双链表"""

    def add(self, item):
        """头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        :param pos: 从0开始
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后，pre指向pos - 1 的位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            # 先判断此结点是否是头节点
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next
