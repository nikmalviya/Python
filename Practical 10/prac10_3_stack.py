
class Stack:
    __stack = []

    def __init__(self, size=10):
        self.__size = size

    def get_size(self):
        return self.__size

    def push(self, value):
        if len(self.__stack) is 10:
            print('Stack OverFlow..')
            return False
        else:
            self.__stack.append(value)
        return True

    def peek(self):
        if len(self.__stack) is 0:
            print('Stack UnderFlow..')
            return
        return self.__stack[-1]

    def pop(self):
        if len(self.__stack) is 0:
            print('Stack UnderFlow..')
        else:
            return self.__stack.pop()

    def __str__(self):
            return f'Stack({self.__stack})'


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(18)
    print(stack)
    stack.push(15)
    stack.push(19)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
