from grid import Grid
from binary_tree import BinaryTree


def main():
    grid = Grid(10, 10)
    BinaryTree.on(grid)
    print(grid)

if __name__ == '__main__':
    main()
