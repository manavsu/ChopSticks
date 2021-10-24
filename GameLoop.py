
from OutputGenerator import OutputGenerator
from Player import Player


class GameLoop:
    def __init__(self, top, bottom):
        self.top_player = top
        self.bottom_player = bottom
        self.output_generator = OutputGenerator(top, bottom)

    def Run(self):
        playing = self.top_player.IsAlive() and self.bottom_player.IsAlive()
        cnt = 1
        while playing:
            attacking_player = self.top_player if cnt % 2 == 0 else self.bottom_player
            defending_player = self.top_player if cnt % 2 != 0 else self.bottom_player
            self.output_generator.OutputState()
            attacking_player.TakeTurn(defending_player)
            playing = self.top_player.IsAlive() and self.bottom_player.IsAlive()
            cnt += 1
        
        self.output_generator.OutputState()
        self.output_generator.PrintResults()