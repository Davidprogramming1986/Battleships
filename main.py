#------------------------------------------------------------------------
#
#               Battleships
#
#------------------------------------------------------------------------

import random

class Grid():

    def __init__(self):
        self.game_grid = []
        self.player_view_grid = []
        self.grid_size = 10
        self.grid_rank = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def init_grid(self):

        for gridY in range(self.grid_size):
            grid_row = []

            for gridX in range(self.grid_size):
                grid_row.append(' - ')

            self.game_grid.append(grid_row)

    def print_grid(self):
        print('  1  2  3  4  5  6  7  8  9  10')

        for gridX in range(len(self.game_grid)):
            print(self.grid_rank[gridX], end='')

            for gridY in range(len(self.game_grid)):
                print(self.game_grid[gridX][gridY], end='')

            print('')

    def print_player_view_grid(self):
        print('  1  2  3  4  5  6  7  8  9  10')

        for gridX in range(len(self.player_view_grid)):
            print(self.grid_rank[gridX], end='')

            for gridY in range(len(self.player_view_grid)):
                print(self.player_view_grid[gridX][gridY], end='')

            print('')


class Ship():

    def __init__(self):
        self.ships = [5, 4, 3, 3, 2, 2]

    def max_random_place(self, grid_size, ship_length):
        return random.randrange(0, (grid_size - ship_length))

    def random_x_or_y(self):
        x_or_y = random.randint(0, 1)
        if x_or_y == 0:
            return 'x'
        return 'y'

    def place_ships(self, grid):
        grid_length = len(grid)

        for ship in self.ships:

            for n in range(10000):
                print('n: ',n)

                randomXY = self.random_x_or_y()
                random_grid_space = random.randrange(grid_length)
                start_point = self.max_random_place(grid_length, ship)

                if randomXY == 'y':
                    spaces_free = True

                    # checks spaces are free and that there is a space gap  on same axis
                    for ship_square in range(ship + 1):
                        square = grid[start_point + ship_square][random_grid_space]
                        if square != ' - ':
                            spaces_free = False

                    if spaces_free:
                        for ship_square in range(ship):
                            grid[start_point + ship_square][random_grid_space] = ' S' + str(ship)

                    elif spaces_free == False:
                        continue

                    break


                if randomXY == 'x':
                    spaces_free = True

                    # checks spaces are free and that there is a space gap on same axis
                    for ship_square in range(ship + 1):
                        square = grid[random_grid_space][start_point + ship_square]
                        if square != ' - ':
                            spaces_free = False

                    if spaces_free:
                        for ship_square in range(ship):
                            grid[random_grid_space][start_point + ship_square] = ' S' + str(ship)

                    elif spaces_free == False:
                        continue

                    break











game = Grid()
ship = Ship()
game.init_grid()
game.player_view_grid = list(game.game_grid)


print('player view')
game.print_player_view_grid()

#ship.place_ships(game.game_grid)
game.game_grid[0][0] = ' D '
game.player_view_grid[0][1]= ' H '
print('player view')
game.print_player_view_grid()
print('game view')
game.print_grid()
print('player view')
game.print_player_view_grid()
print(game.david)