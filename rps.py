#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
cycleMoves = ['rock', 'paper', 'scissors']
count = 0

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'
        
    def learn(self, my_move, their_move):
        self.remember = their_move

# a subclass called RandomPlayer that chooses moves
# at Random from 'moves'([rock, paper, scissors])
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# a subclass for a human player that takes input from a 
# human and validates input as 'rock', 'paper', 'scissors
class HumanPlayer(Player):
    def move(self):
        response = input("Enter 'rock', 'paper' or 'scissors': ").lower()
        if response in moves:
             return response
        else:
            self.move()

# a ReflectPlayer subclass that remembers what move the opponent
#  player made in the last round and plays that move this round
class ReflectPlayer(Player):
    def move(self):
        global count
        print(f"RP Count: {count}")
        if count == 0:
            play = random.choice(moves)
            return play  
        else: 
            return self.remember

# a CyclePlayer subclass that remembers the move it made in the 
# last rounds and cycles through the moves
class CyclePlayer(Player):
    def move(self):
        play = cycleMoves.pop(cycleMoves.index(random.choice(cycleMoves)))
        return play

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#TODO keep score

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        global count
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        count += 1
        print(f"Count: {count}")
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
