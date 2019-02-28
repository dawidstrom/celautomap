import random as rand
import pdb

# Arbitrarily named tiles, '*' denotes an empty tile.
#tile_types = ['*', '1', '2', '3', '4', '5', '6']
tile_types = ['*', '1', '2']

class Board:
    def __init__(self, size):
        #self.board = self.__rand_board(size)
        self.board = self.__perlin_board(size)

    def evolve(self):
        """
        Evolves the board based on tile specific rules.
        """
        evolved_board = []
        for y in range(len(self.board)):
            evolved_row = []
            for x in range(len(self.board[y])):
                # Get neighbouring tiles.
                neighbours = self.__kernel(self.board, (x,y))

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

    def __kernel(self, board, pos):
        """
        Returns the 3x3 matrix of tiles centered at 'pos' in the board. Gives
        None for neighbours outside the board.

        board {[[char]]}: A 2D board of tiles, each tile represented by a char.
        pos {(int,int)}: The x,y position on the board.
        """
        kernel = []
        for y in range(-1,2): # Will give [-1,0,1] to get neighbours.
            for x in range(-1,2): # Will give [-1,0,1] to get neighbours.
                if pos[1]+y < 0 or \
                   pos[1]+y >= len(board) or \
                   pos[0]+x < 0 or \
                   pos[0]+x >= len(board[pos[1]]):
                    kernel.append(None) # Neighbour is outside the board.
                else:
                    kernel.append(board[pos[1]+y][pos[0]+x])
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

    def __perlin_board(self, size):
        """
        Returns a board with tiles based on random heightmap.

        size {(int,int)}: size of board to be generated.
        """

        # Generate gradient values.
        gradient_board = []
        for y in range(size[1]):
            gradient_row = []
            for x in range(size[0]):
                r = rand.random() * 2 -1 # Gives value between -1.0 and 1.0.
                gradient_row.append(r)
            gradient_board.append(gradient_row)
        
        # Calculate smoothed board.
        height_board = []
        for y in range(size[1]):
            height_row = []
            for x in range(size[0]):
                neighbours = self.__kernel(gradient_board, (x,y))
                # Remove None entries.
                neighbours = [x for x in neighbours if x is not None]
                
                height_row.append(sum(neighbours))
            height_board.append(height_row)

        # Decide on what tile to use based on height.
        tile_board = []
        for y in range(size[1]):
            tile_row = []
            for x in range(size[0]):
                # Example tile strategy.
                # TODO: Dynamic tiling strategy.
                if height_board[y][x] < -1: # Waterline.
                    tile_row.append('1')
                elif height_board[y][x] < 1: # Ground.
                    tile_row.append('*')
                else: # Mountain.
                    tile_row.append('2')
            tile_board.append(tile_row)

        return tile_board

            
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
