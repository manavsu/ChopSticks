from Player import Player
from GameLoop import GameLoop

def CreatePlayer(number):
    name = input("What is Player " + str(number) + "'s name? ") 
    return Player(name)

def GetMove(player, opponent):
    raise NotImplementedError

def __main__():
    print("Welcome To Chopsticks")
    player_1 = CreatePlayer(1)
    player_2 = Player("Computer")
    game_loop = GameLoop(player_1, player_2)
    play_again = True
    while play_again:
        game_loop.Run()
        play_again = input("Would You Like To Play Again? (Y/N) ").lower() == "y"
        player_1.Reset()
        player_2.Reset()

__main__()

