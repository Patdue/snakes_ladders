from __future__ import annotations
from typing import List

from figure import Figure

class Field:
    """
    A single field in a game board.
    """
    def __init__(self):
        self._figures: List['Figure'] = []

    def place_figure(self, figure: Figure):
        self._figures.append(figure)
        figure.history.append(self)

    def remove_figure(self, figure: Figure):
        return self._figures.remove(figure)

    def trigger(self) -> Field:
        """
        Trigger a move, when a figure enters this field.
        """
        # TODO if is occupied, back to start
        return self

    def is_empty(self):
        return not self._figures

    def __repr__(self):
        return "Field(figures="+repr(self._figures)+")"


class Shortcut(Field):
    """
    A shortcut transports the player to the target when triggered.
    """
    def __init__(self, target = None):
        self.target: Field = target
        super().__init__()

    def trigger(self) -> Field:
        return self.target


class Snake(Shortcut):
    """
    Snakes are backward shortcuts.
    """
    # TODO assertion target before self
    def __repr__(self):
        return "Snake(figures="+repr(self._figures)+",target="+repr(self.target)+")"


class Ladder(Shortcut):
    """
    Ladders are forward shortcuts
    """
    # TODO assertion target after self
    def __repr__(self):
        return "Ladder(figures="+repr(self._figures)+",target="+repr(self.target)+")"
