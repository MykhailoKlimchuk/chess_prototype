from chess.figures.figure import Figure


class Pawn(Figure):
    def __init__(self, *args, **kwargs):
        super(Pawn, self).__init__(*args, **kwargs)
        self.mega_step = False

    def check_move(self, cell_to):
        from_x, from_y = self.cell.coordinate
        to_x, to_y = cell_to.coordinate

        if from_x == to_x and from_y == to_y - 1:
            return True

        if from_x == to_x and from_y == to_y - 2 and from_y == 2:
            return True

        if (from_x == to_x + 1 or from_x == to_x - 1) and from_y == to_y - 1 and \
            cell_to.figure and cell_to.figure.user != self.user:
            return True

        return False
