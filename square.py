class Square:
    # Status numbers:
    # 0->6 = Empty square with THAT amount of mines around it
    # 8 and 7 squares will not be considered this is a beginner mode
    # where the probability of having a 7 or 8 square is way too low
    # It would be much better to not consider them to reduce scanning time
    # 9 = unopened square
    # 10 = mine
    # 11 = flagged square

    status = 10
    xcoord = 0
    ycoord = 0

    def __init__(self, xcoord, ycoord, status):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.status = status

    def __str__(self):
        return f"{self.status}"

    def set_status(self, status):
        self.status = status

    def flag(self):
        self.status = 11
