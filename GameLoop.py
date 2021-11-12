
from OutputGenerator import OutputGenerator
from Player import Player


class GameLoop:
    def __init__(self, top, bottom):
        self.top_player = top
        self.bottom_player = bottom
        self.output_generator = OutputGenerator(top, bottom)

    def Run(self, silent=False):
        playing = self.top_player.IsAlive() and self.bottom_player.IsAlive()
        cnt = 1
        while playing:
            attacking_player = self.top_player if cnt % 2 == 0 else self.bottom_player
            defending_player = self.top_player if cnt % 2 != 0 else self.bottom_player
            if not silent:
                self.output_generator.OutputState()
            attacking_player.TakeTurn(defending_player, silent)
            playing = self.top_player.IsAlive() and self.bottom_player.IsAlive()
            cnt += 1
        if not silent:
            self.output_generator.OutputState()
            self.output_generator.PrintResults()
    
    def GetResults(self):
        return self.top_player.name if self.top_player.IsAlive() else self.bottom_player.name