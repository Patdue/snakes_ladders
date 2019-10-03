import logging

from board import Board
from die import Die
from figure import Figure
from game import Game


logging.basicConfig(level=logging.INFO)
figures = [Figure(name="Päde"), Figure(name="Raffi")]
game = Game(board=Board.get_random_board(), die = Die(), figures=figures)

result = game.run()

print(result)
