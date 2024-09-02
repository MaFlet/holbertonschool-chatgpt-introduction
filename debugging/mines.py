#!/usr/bin/python3
"""
Script to print and play minesweeper in the console
"""
import random
import os

def clear_screen():
    """
    Clears the console screen based on the operating system
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    """
    Class to initialize and manage the minesweeper game.
    """
    def __init__(self, width=10, height=10, mines=10):
        """
        Initializes the minesweeper game with the given width, height, and number of mines.
        :param width: Width of the game board.
        :param height: Height of the game board.
        :param mines: Number of mines to place on the board.
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """
        Prints the game board. Reveals all cells if 'reveal' is True.
        :param reveal: If True, reveals all cells; otherwise, only revealed cells.
        """
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if y * self.width + x in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """
        Counts the number of mines in the adjacent cells around the given cell.
        :param x: X-coordinate of the cell.
        :param y: Y-coordinate of the cell.
        :return: The number of adjacent mines.
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if ny * self.width + nx in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveals the cell at the specified coordinates.
        If the cell is empty, recursively reveals adjacent cells.
        :param x: X-coordinate of the cell to reveal.
        :param y: Y-coordinate of the cell to reveal.
        :return: True if the cell was succesfully revealed; False if it contains a mine.
        """
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("Coordinates out of bounds. Try again.")
            return True
        if y * self.width + x in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True
    def check_win(self):
        """
        Checks if all non-mine cells have revealed, indicating a win.
        :return: True if the player has won; False otherwise.
        """
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        """
        Main game loop for player interaction with the board.
        """
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You won.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
