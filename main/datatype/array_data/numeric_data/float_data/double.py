from main.datatype.array_data.numeric_data.float import Float


class Double(Float):
    def __init__(self, value, size=None):
        super().__init__(value, size)
        self.Value = [float(i) for i in self]

    def __str__(self):
        if self.Size == (0, 0):
            return "     []"
        if self.n == 0:
            return "  1×0 empty double row vector"
        if all((int(i) == i) for i in self):
            max_len = max(len(str(int(i))) for i in self)
            if max_len <= 3:
                return self.to_string(self.__show, width=6, precision=0)
            elif max_len <= 8:
                return self.to_string(self.__show, width=12, precision=0)
        return self.to_string(self.__show)
        # todo: scientific notation for too big or too small

    @staticmethod
    def __show(item, width=10, precision=4):
        return f"{item:>{width}.{precision}f}"