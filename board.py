import random as rand
import pdb

# Arbitrarily named tiles, '*' denotes an empty tile.
#tile_types = ['*', '1', '2', '3', '4', '5', '6']
tile_types = ['*', '1', '2']

class Board:
    def __init__(self, size):
        self.board = self.__rand_board(size)

    def evolve(self):
        """
        Evolves the board based on tile specific rules.
        """
        evolved_board = []
        for y in range(len(self.board)):
            evolved_row = []
            for x in range(len(self.board[y])):
                neighbours = self.__kernel((x,y)) # Get neighbouring tiles.

                # Random rules to illustrate the point.
                # TODO: Dynamically defined rules.
                new_tile = self.board[y][x]
                if neighbours.count('*') > 2:
                    new_tile = '1'
                if neighbours.count('1') > 4:
                    new_tile = '2'
                if neighbours.count('2') > 3:
                    new_tile = '*'
                evolved_row.append(new_tile)

            evolved_board.append(evolved_row)

        self.board = evolved_board

    def __kernel(self, pos):
        """
        Returns the 3x3 matrix of tiles centered at 'pos' in the board. Gives
        None for neighbours outside the board.

        pos {(int,int)}: The x,y position on the board.
        """
        kernel = []
        for y in range(-1,2): # Will give [-1,0,1] to get neighbours.
            for x in range(-1,2): # Will give [-1,0,1] to get neighbours.
                if pos[1]+y < 0 or \
                   pos[1]+y >= len(self.board) or \
                   pos[0]+x < 0 or \
                   pos[0]+x >= len(self.board[pos[1]]):
                    kernel.append(None) # Neighbour is outside the board.
                else:
                    kernel.append(self.board[pos[1]+y][pos[0]+x])
        return kernel


    def __rand_board(self, size):
        """
        Returns a board of random tiles.

        size {(int,int)}: size of board to be generated.
        """
        board = []
        for y in range(size[1]):
            row = []
            for x in range(size[0]):
                rand_index = rand.randrange(len(tile_types))
                row.append(tile_types[rand_index])
            board.append(row)

        return board
            
    def __str__(self):
        string = ""
        for row in self.board:
            for tile in row:
                string += tile + ' '
            string += '\n'
        return string

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    board = Board((10,10))
    print(board)
    board.evolve()
    print(board)
    board.evolve()
    print(board)
    board.evolve()
    print(board)
    board.evolve()
    print(board)
    board.evolve()
    print(board)
