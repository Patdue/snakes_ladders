from __future__ import annotations
from typing import List

from die import Die


class Figure:
    """
    A figure to move around the board.
    """

    def __init__(self, name: str):
        self.name = name
        self.history: List['Field'] = []

    @property
    def current_field(self):
        return self.history[-1]

    @current_field.setter
    def current_field(self, field: 'Field'):
        self.current_field.remove_figure(self)
        field.place_figure(self)

    def play_turn(self, die: Die, board: 'Board'):
        """"""
        roll = die.roll()
        move_to = board.get_next(self.current_field, roll)
        self.current_field = move_to


    def __repr__(self):
        return "Figure({})".format(self.name)
