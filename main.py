from Player import Player
from GameLoop import GameLoop

use_ai = False

def CreatePlayer(number):
    name = input("What is Player " + str(number) + "'s name? ") 
    return Player(name, use_ai)

def __main__():
    print("Welcome To Chopsticks")
    print("The Winner Will Survive On The Next Round")
    print("The Loser May Or May Not Be Have Their Brain Introduced To A Super Sonic Piece Of Metal")
    player_1 = CreatePlayer(1)
    player_2 = CreatePlayer(2)
    game_loop = GameLoop(player_1, player_2)
    play_again = True
    while play_again:
        game_loop.Run()
        play_again = input("Would You Like To Play Again? (Y/N) ").lower() == "y"
        player_1.Reset()
        player_2.Reset()

__main__()

