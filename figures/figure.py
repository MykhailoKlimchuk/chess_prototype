from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, id_, user, cell):
        self.id = id_
        self.user = user
        self.cell = cell

    @abstractmethod
    def check_move(self, cell_to) -> bool:
        """
        can figure move from self.cell to cell_to
        :param cell_to:
        :return:
        """
        pass

    def move_to_cell(self, cell_to):
        self.cell.figure = None
        self.cell = cell_to
        cell_to.figure = self


# TODO check is_empty cell