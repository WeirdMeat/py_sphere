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

    __radd__ = __add__

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)
