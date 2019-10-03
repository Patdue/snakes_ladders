from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from itertools import cycle
from typing import List

from board import Board
from die import Die
from figure import Figure


@dataclass
class Game:
    board: Board
    die: Die
    figures: List[Figure]

    def run(self) -> List[Figure]:
        self.board.initialize(self.figures)
        figure_cycle = cycle(self.figures)

        while True:
            print(self.board)
            current_figure = next(figure_cycle)
            time.sleep(1)
            current_figure.play_turn(self.die, self.board)

            if self.is_over():
                break

        print(self.board)
        return self.compute_leaderboard()


    def is_over(self):
        return not self.board.is_last_field_empty()

    def compute_leaderboard(self) -> List[Figure]:
        return sorted(self.figures, key=lambda x: self.score(x))

    def score(self, figure: Figure) -> int:
        return self.board.score(figure.current_field)
