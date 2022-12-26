import numpy
from square import Square


class Board:
    arr = numpy.empty(64, dtype=Square)

    def __init__(self):
        k = -1
        for y in range(8):
            for x in range(8):
                k += 1
                self.arr[k] = Square(x, y, 10)

    def __str__(self):
        to_string = ""
        k = -1
        for i in range(8):
            for j in range(8):
                k += 1
                if k % 8 == 0:
                    to_string = to_string + "[" + f"{self.arr[k]}, "
                elif k % 8 == 7:
                    to_string = to_string + f"{self.arr[k]}]\n"
                else:
                    to_string = to_string + f"{self.arr[k]}, "
        return to_string
