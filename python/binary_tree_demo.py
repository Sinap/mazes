# -*- coding: utf-8 -*-
from grid import Grid
from binary_tree import BinaryTree


def main():
    grid = Grid(4, 4)
    BinaryTree.on(grid)
    print(grid)

if __name__ == '__main__':
    main()
