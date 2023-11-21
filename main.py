class PopError(Exception):
    pass


class TypesMismatchError(Exception):
    pass


class Stack:

    def __init__(self):
        self.__stack = []
        self.__type_val = None

    def push(self, val):
        if len(self.__stack) == 0:
            self.__stack.append(val)
            self.__type_val = type(val)
        else:
            if self.__type_val == type(val):
                self.__stack.append(val)
            else:
                raise TypesMismatchError(f"Ожидается тип {self.__type_val}. Пользователь пытается внести тип {type(val)}")

    def pop(self):
        if len(self.__stack) != 0:
            return self.__stack.pop()
        else:
            raise PopError("Стек пуст")


stack = Stack()

stack.push(1)
stack.push("hjg")

print(stack.pop())
print(stack.pop())
print(stack.pop())

