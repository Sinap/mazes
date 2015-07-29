# -*- coding: utf-8 -*-


class Cell(object):
    """
    Represents a single cell in a grid
    """

    def __init__(self, row, column):
        super(Cell, self).__init__()
        self.row = row
        self.column = column
        self._links = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    @property
    def links(self):
        return self._links.keys

    def link(self, cell, bidi=True):
        self._links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self._links.pop(cell, None)
        if bidi:
            cell.unlink(self, False)

    def neighbors(self):
        l = []
        if self.north:
            l.append(self.north)
        if self.south:
            l.append(self.south)
        if self.east:
            l.append(self.east)
        if self.west:
            l.append(self.west)
        return l

    def __contains__(self, cell):
        return self._links.get(cell, False)

    def __str__(self):
        return 'row: %i column: %i' % (self.row, self.column)
