from chess.figures.figure import Figure


class Horse(Figure):
    def check_move(self, cell_to) -> bool:
        from_x, from_y = self.cell.coordinate
        to_x, to_y = cell_to.coordinate

        if ((from_y == to_y - 2 or from_y == to_y + 2) and (from_x == to_x - 1 or from_x == to_x + 1)) or \
                ((from_y == to_y - 1 or from_y == to_y + 1) and (from_x == to_x - 2 or from_x == to_x + 2)):
            return True
        return False
