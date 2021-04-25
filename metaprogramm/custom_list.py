class CustomList(list):
    def __add__(self, other):
        if len(self) > len(other):
            first, second = self.copy(), other.copy()
        else:
            first, second = other.copy(), self.copy()
        second += [0] * (len(self) - len(other))
        res = CustomList()
        for i, j in zip(first, second):
            res.append(i + j)
        return res

    def __neg__(self):
        res = CustomList()
        for i in self:
            res.append(-i)
        return res

    def __sub__(self, other):
        return self.__neg__().__add__(other).__neg__()

    def __rsub__(self, other):
        return self.__sub__(other).__neg__()

    __radd__ = __add__

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)
