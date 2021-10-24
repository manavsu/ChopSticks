
class OutputGenerator:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def OutputState(self):
        print(self.top)
        print(self.bottom)

    def PrintResults(self):
        assert not (self.top.IsAlive() and self.bottom.IsAlive()), "Someone Must Be Terminated Before Results Can Be Announced"
        if self.top.IsAlive():
            winner = self.top
        else:
            winner = self.bottom
        
        print("The Winner is: " + winner.name)