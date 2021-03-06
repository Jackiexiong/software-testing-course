class Stack(object):
    def __init__(self):
        self.__values = []
        self.__len = 0

    def push(self, v):
        if v == None:
            raise ValueError("Unsupported value: {0}".format(v))
        self.__values.append(v)
        self.__len += 1     

    def pop(self):
        if not self.__values:
            return 0
        else:
            self.__len -= 1
            return self.__values.pop()

    def len(self):
        return self.__len

