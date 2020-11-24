#!/usr/bin/env python3
import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
moves = ['rock', 'paper', 'scissors']
cycleMoves = ['rock', 'paper', 'scissors']
count = 0
player1_score = 0
player2_score = 0

"""The Player class is the parent class for all of the Players
in this game"""
def pause():
    time.sleep(1)

class Player:
    def move(self):
        return 'rock'
        
    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.remember = self.their_move

    def score(self, my_move, their_move):
        global player1_score, player2_score
        self.my_move = my_move
        self.their_move = their_move

        if self.my_move == self.their_move:
            print("It is a tie, no score")
            pause()
        elif beats(self.my_move, self.their_move):
            print("Player one wins")
            pause()
            player1_score += 1
        else:
            print("Player two wins")
            pause()
            player2_score += 1

        print(f"Player One: {player1_score}  Player Two: {player2_score}\n")
        pause()

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
        pause()
        if response in moves:
             return response
        else:
            self.move()

# a ReflectPlayer subclass that remembers what move the opponent
#  player made in the last round and plays that move this round
class ReflectPlayer(Player):
    def move(self):
        global count
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
    if one != two:
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))
        

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        global count
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        pause()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        count += 1
        self.p1.score(move1, move2)
        pause()

    def win(self, total1, total2):
        self.total1 = total1
        self.total2 = total2

        if self.total1 > self.total2:
            print("Player One Wins!\n")
            pause()
        elif self.total1 < self.total2:
            print("Player Two Wins!\n")
            pause()
        else:
            print("It is a tie, no one wins...")

    def play_game(self):
        print("Game start!\n")
        pause()
        for round in range(3):
            print(f"Round {round}:")
            pause()
            self.play_round()
        self.win(player1_score, player2_score)
        print("Game over!")


if __name__ == '__main__':
    # game play will utilize a HumanPlayer for input and randomly
    # pick an opponent from the list of opponents
    opponents = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(opponents))
    game.play_game()
