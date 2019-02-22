# coding:utf-8

class Stack(object):
    def __init__(self):
        # 创建一个新的空栈
        self.stack = []

    def push(self, item):
        # 添加一个新的元素item到栈顶
        return self.stack.append(item)

    def pop(self):
        # 弹出栈顶元素
        return self.stack.pop()

    def peek(self):
        return self.stack[self.size() - 1]
        # 返回栈顶元素

    def is_empty(self):
        # 判断栈是否为空
        return self.stack is []

    def size(self):
        # 返回栈的元素个数
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(5)
    stack.push(15)
    print(stack.peek())
    print(stack.size())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
