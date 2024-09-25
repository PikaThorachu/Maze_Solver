from cell import Cell

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
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for cell in self._cells:
            cell._draw_cell()
                
        # Step 1: start at (x1, y1), add cell size x and y to get the second point for the cell. Create cell 1, num rows -= 1
        # Step 2: add cell size y to y1, start second cell at x1, y2, then repeat step 1.
        # Step 3 - continue looping until num rows == 0

        # Step 4: complete steps 1-3 for col 1, then num cols -= 1
        # Step 5: repeat step for until num cols == 0


    def _draw_cell(self, i, j):
        # This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself. The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        pass

    def _animate(self):
        # The animate method is what allows us to visualize what the algorithms are doing in real time. It should simply call the window's redraw() method, then sleep for a short amount of time so your eyes keep up with each render frame. I slept for 0.05 seconds.
        pass
