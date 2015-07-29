# -*- coding: utf-8 -*-
import random


class Sidewinder(object):
    """
    docstring for Sidewinder
    """

    @staticmethod
    def on(grid):
        for row in grid.each_row():
            run = []

            for cell in row:
                run.append(cell)

                at_eastern_boundary = (cell.east is None)
                at_northern_boundary = (cell.north is None)

                should_close_out = at_eastern_boundary or (not at_northern_boundary and random.choice(range(2)) == 0)

                if should_close_out:
                    member = random.choice(run)
                    if member.north:
                        member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)
        return grid
