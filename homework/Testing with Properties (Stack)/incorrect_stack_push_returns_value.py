class Stack(object):
    def __init__(self):
        self.__values = []

    def push(self, v):
        if v == None:
            raise ValueError("Unsupported value: {0}".format(v))
        top = self.__values[-1:]
        self.__values.append(v)
        return top

    def pop(self):
        if len(self.__values) == 0:
            return None
        else:
            return self.__values.pop()

    def len(self):
        return len(self.__values)

