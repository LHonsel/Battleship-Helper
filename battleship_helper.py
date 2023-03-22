import numpy as np
import random

class battleship_helper:

    def __init__(self, grid = np.ones((10,10)), list_ships = [5,4,3,3,2]):
        self.grid = grid
        self.list_ships = list_ships
        self.sunk_ships = []

    def missed_hit(self, x, y):
        """
        Modify the possibility grid in place by replacing a 1 with a zero
        :param coordinates: The coordinates of the hit.
        :return: Returns error if cell already hit. Otherwise, modifies the grid in place.
        """
        assert self.grid[x,y] == 1, "You cannot hit the same target twice"
        self.grid[x,y] = 0

    def target_hit(self, x, y):
        Modify the grid in place by replacing a 1 with a zero
        :param coordinates: The coordinates of the hit.
        :return: Returns error if cell already hit. Otherwise, modifies the grid in place.
        """
        assert self.grid[x,y] == 1, "You cannot hit the same target twice"
        self.grid[x, y] = 2

    def ship_sunk_hit(self, x, y):
        """
        If a hit leads to a ship being sunk, the latest hit cell becomes a 3, the previous cells marked as 2s into 3s (sunk ship),
        and we remove that ship from the ship list.
        :param coordinates: The coordinates of the hit.
        :return: Returns error if cell already hit. Otherwise, modifies the grid in place.
        """
        assert self.grid[x,y] == 1, "You cannot hit the same target twice"
        self.grid[x, y] = 3
        x_left, y_up = (x - 1), (y - 1)
        x_right, y_down = (x + 2), (y + 2)
        size_sunk_ship = 1
        while True:
            closest_square = self.grid[x_left:x_right, y_up:y_down]
            location_previous_hit = np.where(closest_square == 2)
            if location_previous_hit[0].size == 0:
                break
            else:
                closest_square[location_previous_hit] = 3
                x_local, y_local = location_previous_hit[0][0], location_previous_hit[1][0]
                x, y = x_left + x_local, y_up + y_local
                x_left, y_up = (x - 1), (y - 1)
                x_right, y_down = (x + 2), (y + 2)
                size_sunk_ship+=1
        self.list_ships.remove(size_sunk_ship)



