# -*- coding: utf-8 -*-
from grid import Grid
from sidewinder import Sidewinder


def main():
    grid = Grid(4, 4)
    Sidewinder.on(grid)
    print(grid)

if __name__ == '__main__':
    main()
