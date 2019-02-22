#coding:utf-8
#创建出单向链表节点
class Node(object):
    def __init__(self, item):
        # 节点前驱
        self.pre = None
        # 数据存储区域
        self.item = item
        # 节点指向区域，指向下一个节点
        self.next = None


class DoubleLinkList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        else:
            # 创建一个临时游标
            cur = self.__head
            count = 0

            while cur is not None:
                # 计数器累加
                count += 1
                # 移动
                cur = cur.next

            return count


    def travel(self):
        '''遍历整个链表'''
        cur = self.__head

        while cur is not None:
            # 打印数据
            print(cur.item, end=" ")
            # 移动游标
            cur = cur.next
        print()


    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            # 让新节点指向旧头结点
            node.next = self.__head
            # 重新设置头结点
            self.__head = node
            # 让旧头结点的前驱指向新的头结点
            node.next.pre = node


    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 创建游标
            cur = self.__head

            while cur.next is not None:
                cur = cur.next
            # 当循环结束，cur指向链表的尾节点
            cur.next = node
            node.pre = cur

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0

            while count < pos - 1:
                count += 1
                cur = cur.next
            # 循环结束，游标停在插入位置前一个节点
            node = Node(item)

            # 让新节点指向其后节点
            node.next = cur.next
            # 让新节点位置之前的节点指向新节点
            cur.next = node
            # 让新节点之前驱节点
            node.pre = cur
            # 让原先位置的节点的前驱指向新节点
            node.next.pre = node

    def remove(self, item):
        '''删除节点'''
        if self.is_empty():
            return
        else:
            # 创建cur游标用于检查是否是要删除的节点
            cur = self.__head

            while cur is not None:

                if cur.item == item:
                    # 当找到要删除的数据的时候
                    if cur == self.__head:
                        # 当要删除的数据在头结点的时候，让head指向头结点的下一个节点
                        self.__head = cur.next
                        if cur.next:
                            # 判断新头结点是否是节点，是节点的话，修改其前驱，将其指向None
                            cur.next.pre = None
                    else:
                        # 要删除的节点在链表的中部或者是尾部，直接让前节点指向当前接的的后续节点
                        cur.pre.next = cur.next
                        if cur.next:
                            # 判断删除节点之后的节点是否存在，如果存在将其前驱指向删除节点的前驱
                            cur.next.pre = cur.pre
                    # 当删除一个节点之后立刻退出(每次只删除一个)
                    break
                else:
                    # 当前节点并不是我们要删除的数据
                    cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''

        cur = self.__head

        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        # 当循环结束，说明在当前链表中找不到数据
        return False


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.add(4)
    dll.travel()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.travel()
    dll.insert(-100,666)
    dll.travel()
    dll.insert(5, 666)
    dll.travel()
    dll.insert(100, 666)
    dll.travel()
    dll.remove(666)
    dll.travel()
    dll.remove(666)
    dll.travel()
    dll.remove(666)
    dll.travel()
    print(dll.search(1))
    print(dll.search(666))