from __future__ import annotations

import logging
import random
from dataclasses import dataclass, field
from typing import List, Dict, Type, Tuple

from field import Field, Shortcut, Snake, Ladder
from figure import Figure


class Board():
    """
    A game board consists of multiple fields.
    """

    def __init__(self, fields: List[Field] = None):
        self.fields: List[Field] = fields if fields else []

    def initialize(self, figures: List[Figure]):
        for figure in figures:
            self.fields[0].place_figure(figure)

    def get_next(self, field: Field, roll: int) -> Field:
        start = self.fields.index(field)
        # TODO overshoot
        next = self.fields[min(start + roll, len(self.fields)-1)]
        return next.trigger()


    def __repr__(self):
        return "Board("+repr(self.fields)+")"

    @staticmethod
    def get_random_board(size: Tuple[int, int] = (3,4),
                         n_shortcuts: Dict[Type[Shortcut], int] = {Snake:1, Ladder:1}) -> 'Board':

        board = Board()
        x, y = size
        n_normal_fields = x * y - sum(n_shortcuts.values())

        for _ in range(n_normal_fields):
            board.fields.append(Field())

        for shortcut in n_shortcuts:
            for _ in range(n_shortcuts[shortcut]):
                snake = shortcut(target=random.choice(board.fields))
                board.fields.insert(random.randint(0, len(board.fields) - 1), snake)
        return board

    def is_last_field_empty(self) -> bool:
        return self.fields[-1].is_empty()

    def score(self, field: Field) -> int:
        return self.fields.index(field)
