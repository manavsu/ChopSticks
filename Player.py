
from enum import Enum


def GetInput(prompt: str) -> str:
    response = input(prompt)
    if response.lower() == "quit" or response.lower() == "exit":
        raise SystemExit

    return response

class Side(Enum):
    LEFT = 0
    RIGHT = 1

    def __str__(self) -> str:
        return self.name

class Player:
    num_fingers = 5
    failed_attack_error = "This Attack Will Achieve Nothing"

    def __init__(self, name, get_move_func=None):
        self.name = name
        self.left = 1
        self.right = 1
        self.GetMove = Player.GetMoveViaInput if get_move_func is None else get_move_func

    def IsAlive(self):
        return self.left > 0 or self.right > 0

    def Reset(self):
        self.left = 1
        self.right = 1

    def TakeTurn(self, opponent):
        attacker, target = self.GetMove(self, opponent)
        self.Attack(opponent, attacker, target)
        print(str(self.name) + " Attacked " + opponent.name + "'s " + str(target) + " With " + str(attacker))

    def GetMoveViaInput(self, opponent):
        assert self.left > 0 or self.right > 0, str(self.name) + " : You Are Already Dead"
        attacker = self.GetSide(str(self.name) + " : Pick A Side To Attack With (L)eft or (R)ight? -> ")
        target = self.GetSide(str(self.name) + " : Target A Side (L)eft or (R)ight? -> ", opponent)
        return (attacker, target)

    def GetSide(self, prompt, subject = None):
        if subject is None:
            subject = self
        if (subject.left == 0) or (subject.right == 0):
            return Side.RIGHT if subject.left == 0 else Side.LEFT

        valid = False
        while not valid:
            valid = True
            side_input = GetInput(prompt)
            match side_input.lower():
                case "l"|"L":
                    side = Side.LEFT
                case "r"|"R":
                    side = Side.RIGHT
                case _:
                    print("Invalid Input, Try Again")
                    valid = False
                    
        return side


    def Attack(self, opponent, attacker, target):
        match target:
            case Side.LEFT:
                self.AttackLeft(opponent, attacker)
            case Side.RIGHT:
                self.AttackRight(opponent, attacker)


    def AttackRight(self, target, attacker):
        assert target.right > 0, Player.failed_attack_error
        if attacker is Side.RIGHT:
            assert self.right > 0, Player.failed_attack_error
            target.right += self.right
            if target.right >= Player.num_fingers:
                target.right = 0
        else:
            assert self.left > 0, Player.failed_attack_error
            target.right += self.left
            if target.right >= Player.num_fingers:
                target.right = 0


    def AttackLeft(self, target, attacker):
        assert target.left > 0, Player.failed_attack_error
        match attacker:
            case Side.RIGHT:
                assert self.right > 0, Player.failed_attack_error
                target.left += self.right
                if target.left >= Player.num_fingers:
                    target.left = 0
            case Side.LEFT:
                assert self.left > 0, Player.failed_attack_error 
                target.left += self.left
                if target.left >= Player.num_fingers:
                    target.left = 0
    
    def __str__(self):
        return str(self.name) + " : " + str(self.left) + " - - " + str(self.right)