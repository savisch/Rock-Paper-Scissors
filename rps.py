
import random
import time

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round


moves = ['rock', 'paper', 'scissors']


def pause():
    time.sleep(1)


class Player:
    def __init__(self):
        self.cycle_count = 0
        self.count = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.remember = self.their_move


# a subclass called RandomPlayer that chooses moves
# at Random from 'moves'([rock, paper, scissors])
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# a subclass for a human player that takes input from a
# human and validates input as 'rock', 'paper', 'scissors
class HumanPlayer(Player):
    name_response = input("What is your name?\n")

    def learn_name(self):
        self.name = self.name_response
        return self.name

    def move(self):
        self.move_response = input(
            "Enter 'rock', 'paper' or 'scissors': "
            ).lower()
        pause()

        if self.move_response in moves:
            return self.move_response
        else:
            return self.move()


# a ReflectPlayer subclass that remembers what move the opponent
#  player made in the last round and plays that move this round
class ReflectPlayer(Player):
    def move(self):
        if self.count == 0:
            play = random.choice(moves)
            self.count += 1
            return play
        else:
            return self.remember


# a CyclePlayer subclass that remembers the move it made in the
# last rounds and cycles through the moves
class CyclePlayer(Player):
    def move(self):
        if self.cycle_count > 2:
            self.cycle_count = 0

        play = moves[self.cycle_count]
        self.cycle_count += 1
        return play


def beats(one, two):
    if one != two:
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.player1_score = 0
        self.player2_score = 0
        self.p1 = p1
        self.p2 = p2

    def rounds_query(self):
        try:
            self.round_response = int(
                input("How many rounds would you like to play?\n")
                )
            return self.round_response
        except ValueError:
            self.rounds_query()

    def learn_rounds(self):
        self.rounds = self.round_response
        return self.rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        name = self.p1.name
        print(f"{name}: {move1}  Phly Killa': {move2}\n")
        pause()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.score(move1, move2)
        pause()

    def score(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        self.name = self.p1.learn_name()

        if self.my_move == self.their_move:
            print("It is a tie, no score.")
            pause()
        elif beats(self.my_move, self.their_move):
            print(f"{self.name} wins!")
            pause()
            self.player1_score += 1
        else:
            print("Phly Killa' wins!")
            pause()
            self.player2_score += 1

        print(
            f"{self.name}: {self.player1_score}  Phly Killa': {self.player2_score}\n"
            )
        pause()

    def win(self, total1, total2):
        self.total1 = total1
        self.total2 = total2

        if self.total1 > self.total2:
            winner = self.p1.learn_name()
            print(f"{winner} Wins The Game!\n")
            pause()
        elif self.total1 < self.total2:
            print("Phly Killa' Wins The Game!\n")
            pause()
        else:
            print("It is a tie, no one wins...")

    def play_game(self):
        name = self.p1.learn_name()
        print(f"\nHello {name}!\n")
        pause()
        print("Your opponent will be chosen at random.")
        pause()
        self.rounds_query()
        print("Let's start the Game!\n")
        pause()

        for round in range(int(self.learn_rounds())):
            print(f"Round {round}:")
            pause()
            self.play_round()
        self.win(self.player1_score, self.player2_score)
        print("Game over!")
        pause()


if __name__ == '__main__':
    # game play will utilize a HumanPlayer for input and randomly
    # pick an opponent from the list of opponents
    opponents = [RandomPlayer(), ReflectPlayer(), CyclePlayer(), Player()]
    game = Game(HumanPlayer(), random.choice(opponents))
    game.play_game()
