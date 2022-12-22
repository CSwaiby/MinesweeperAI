class Square:
    # Status numbers:
    # 0->6 = Empty square with THAT amount of mines around it
    # 8 and 7 squares will not be considered this is a beginner mode
    # where the probability of having a 7 or 8 square is way too low
    # It would be much better to not consider them to reduce scanning time
    # 9 = mine
    # 10 = unopened square
    # 11 = flagged square

    status = 10
    coord = [0, 0]

    def __init__(self, xcoord, ycoord, status):
        self.status = status
        self.coord = [xcoord, ycoord]

    def __str__(self):
        return f"{self.status}"

    def set_status(self, status):
        self.status = status
