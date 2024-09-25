from cell import Cell
import copy
from time import sleep

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):  # iterates over column number
            col = []
            for j in range(self.num_rows):  # iterates over row number
                x1 = self.x1 + (self.cell_size_x * i)  # i tracks rows
                y1 = self.y1 + (self.cell_size_y * j)  # j tracks cols
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2)
                col.append(cell)
            self._cells.append(col)  # append column after row completion
        for i, col in enumerate(self._cells):
            for j, cell in enumerate(col):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Calculate cell position
        x_position = self.x1 + i * self.cell_size_x
        y_position = self.y1 + j * self.cell_size_y
    
        # Assuming Cell has a 'draw' method to visualize itself
        cell = self._cells[i][j]
        cell.draw(x_position, y_position)
    
        # Trigger animation
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
