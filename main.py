from Player import Player
from GameLoop import GameLoop
from Player import Side

def CreatePlayer(number):
    name = input("What is Player " + str(number) + "'s name? ") 
    return Player(name)

def GetRandomMove(player, opponent):
    """
    Returns a random move for the computer
    """
    import random
    if player.right == 0:
        if opponent.right == 0:
            return (Side.LEFT, Side.LEFT)
        if opponent.left == 0:
            return (Side.LEFT, Side.RIGHT)
        return (Side.LEFT, random.choice([Side.LEFT, Side.RIGHT]))
    if player.left == 0:
        if opponent.right == 0:
            return (Side.RIGHT, Side.LEFT)
        if opponent.left == 0:
            return (Side.RIGHT, Side.RIGHT)
        return (Side.RIGHT, random.choice([Side.LEFT, Side.RIGHT]))
    if opponent.right == 0:
        return (random.choice([Side.LEFT, Side.RIGHT]), Side.LEFT)
    if opponent.left == 0:
        return (random.choice([Side.LEFT, Side.RIGHT]), Side.RIGHT)
    return (random.choice([Side.LEFT, Side.RIGHT]), random.choice([Side.LEFT, Side.RIGHT]))

def GetMove(player, opponent):
    """
    User .right and .left to access the players and opponents hands

    Returns the next move for the player (Attacking Side, Targeting Side),
    use the Enum Side.LEFT or Side.RIGHT
    """
    raise NotImplementedError

def PlayGame():
    """Player a game manually."""
    print("Welcome To Chopsticks")
    player_1 = CreatePlayer(1)
    player_2 = Player("Computer", GetRandomMove)
    game_loop = GameLoop(player_1, player_2)
    play_again = True
    while play_again:
        game_loop.Run()
        play_again = input("Would You Like To Play Again? (Y/N) ").lower() == "y"
        player_1.Reset()
        player_2.Reset()

def PlayAutomated(count, player_1, player_2):
    player_1_wins = 0
    for i in range(count):
        game_loop = GameLoop(player_1, player_2)
        game_loop.Run(silent=True)
        winner = game_loop.GetResults()
        if winner == player_1.name:
            player_1_wins += 1
        player_1.Reset()
        player_2.Reset()
    print(player_1.name + " win percentage :" + str(player_1_wins * 100/count) + "%")

def __main__():
    PlayAutomated(100, Player("AlsoComputer", GetRandomMove), Player("Computer", GetRandomMove))
    


__main__()

