from cell import Cell


class Grid(object):
    """
    docstring for Grid
    """

    def __init__(self, rows, columns):
        super(Grid, self).__init__()
        self._rows = rows
        self._columns = columns

        self._grid = self._prepare_grid()
        self._configure_cells()

    def each_row(self):
        for row in self._grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if cell:
                    yield cell

    def get(self, row, column):
        if row < 0 or row > self._rows - 1:
            return None
        if column < 0 or column > self._columns - 1:
            return None
        return self._grid[row][column]

    def _prepare_grid(self):
        grid = []
        for row in range(self._rows):
            grid.append([Cell(row, column) for column in range(self._columns)])
        return grid

    def _configure_cells(self):
        for cell in self.each_cell():
            row = cell.row
            col = cell.column

            cell.north = self.get(row - 1, col)
            cell.south = self.get(row + 1, col)
            cell.east = self.get(row, col - 1)
            cell.west = self.get(row, col + 1)

    def __len__(self):
        return self._rows * self._columns

    def __str__(self):
        output = '+' + '---+' * self._columns + '\n'
        for row in self.each_row():
            top = '|'
            bottom = '+'

            for cell in row:
                if cell.east in cell:
                    east_boundary = ' '
                else:
                    east_boundary = '|'
                top += '   ' + east_boundary

                if cell.south in cell:
                    south_boundary = '   '
                else:
                    south_boundary = '---'

                bottom += south_boundary + '+'

            output += top + '\n'
            output += bottom + '\n'
        return output
