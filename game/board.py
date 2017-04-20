"""
Farbod Shahinfar
Pentago Game

"""


class Board:
    """
    pentago board class
    """

    def __init__(self):
        # create an empty board
        self.grid = [Quarter(), Quarter(), Quarter(), Quarter()]

    def insert(self, row, column, player):
        """
        insert a marble in given position
        may raise exception if try to insert in an filled place
        :param row: which row of the game board
        :param column: which column of the game board
        :param player: which player is inserting
        :return: None
        """
        quarter = 2 * (row // 3) + (column // 3)
        self.quarter_insert(quarter, row % 3, column % 3, player)

    def quarter_insert(self, quarter, row, column, player):
        """
        insert a marble in given position
        may raise exception if try to insert in an filled place
        :param quarter: which quarter of the game
        :param row: which row of quarter
        :param column: which column of quarter
        :param player: which player is inserting
        :return: None
        """
        self.grid[quarter].insert(row, column, player)

    def rotate(self, quarter, direction):
        self.grid[quarter].rotate(direction)

    def is_cell_filled(self, row, col):
        quarter = 2 * (row // 3) + (col // 3)
        if self.grid[quarter].get_cell(row % 3, col % 3) != 0:
            return True
        return False

    def get_cell(self, row, col):
        quarter = 2 * (row // 3) + (col // 3)
        return self.grid[quarter].get_cell(row % 3, col % 3)

    def get_row(self, row):
        if row < 0 or row > 5:
            raise GameException("row is between 0 and 5")
        elif row < 3:
            return list(self.grid[0].get_row(row)) + list(self.grid[1].get_row(row))
        elif row < 6:
            return list(self.grid[2].get_row(row % 3)) + list(self.grid[3].get_row(row % 3))

    def get_column(self, col):
        if col < 0 or col > 5:
            raise GameException("row is between 0 and 5")
        elif col < 3:
            return list(self.grid[0].get_col(col)) + list(self.grid[2].get_col(col))
        elif col < 6:
            return list(self.grid[1].get_col(col % 3)) + list(self.grid[3].get_col(col % 3))

    def __str__(self):
        s = [str(x) for x in [self.grid[i] for i in range(4)]]
        string = ""
        for i in range(2):
            for j in range(3):
                string += s[2 * i][6 * j:6 * j + 6] + s[2 * i + 1][6 * j:6 * j + 6]
        return string

    def show(self):
        string = str(self).split(",")
        print("\n" * 2)
        for i in range(6):
            print("\t" * 2, end="")
            for j in range(6):
                print(string[6 * i + j], end=" ")
                if j == 2:
                    print("| ", end="")
            print()  # go to next line
            if i == 2:
                print("\t" * 2, end="")
                print("--" * 6)
        print("\n" * 2)

    def set(self, string):

        q = ["", "", "", ""]
        for i in range(2):
            for j in range(3):
                q[2 * i] += string[(36 * i) + (12 * j):(36 * i) + (12 * j + 6)]
                q[2 * i + 1] += string[(36 * i) + (12 * j + 6):(36 * i) + (12 * j + 12)]
        for i in range(4):
            self.grid[i].set(q[i])

    def is_filled(self):
        for i in range(4):
            if not self.grid[i].is_filled():
                return False
        return True

    def check_win(self):
        winners = set()
        # check row match
        for i in range(6):
            row = self.get_row(i)
            player1_count = row.count(1)
            player2_count = row.count(2)
            if player1_count > 4 or player2_count > 4:  # if there is at least 5 marbles
                if player1_count == 6 or player2_count == 6:  # a full row
                    winners.add(row[0])
                elif row[0] == row[1] and row[-1] == row[-2]:  # we don't have a winner
                    continue
                else:
                    if row[1] == row[2] and row[-2] == row[-3]:
                        if player1_count > player2_count:
                            winners.add(1)
                        else:
                            winners.add(2)
        # check column match
        for i in range(6):
            col = self.get_column(i)
            player1_count = col.count(1)
            player2_count = col.count(2)
            if player1_count > 4 or player2_count > 4:  # if there is at least 5 marbles
                if player1_count == 6 or player2_count == 6:  # a full row
                    winners.add(col[0])
                elif col[0] == col[1] and col[-1] == col[-2]:  # we don't have a winner
                    continue
                else:
                    if col[1] == col[2] and col[-2] == col[-3]:
                        if player1_count > player2_count:
                            winners.add(1)
                        else:
                            winners.add(2)
        # check diagonal match( m = -1)
        diagonal = [self.get_cell(i, i) for i in range(6)]  # Big Diagonal
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is at least 5 marbles
            if player1_count == 6 or player2_count == 6:  # a full row
                winners.add(diagonal[0])
            elif not (diagonal[0] == diagonal[1] and diagonal[-1] == diagonal[-2]):
                if diagonal[1] == diagonal[2] and diagonal[-2] == diagonal[-3]:
                    if player1_count > player2_count:
                        winners.add(1)
                    else:
                        winners.add(2)
        diagonal = [self.get_cell(i, i + 1) for i in range(5)]  # Small Diagonal Up
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is 5 marbles
            winners.add(diagonal[0])
        diagonal = [self.get_cell(i + 1, i) for i in range(5)]  # Small Diagonal Down
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is 5 marbles
            winners.add(diagonal[0])
        # check diagonal match( m = 1)
        diagonal = [self.get_cell(i, 5 - i) for i in range(6)]  # Big Diagonal
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is at least 5 marbles
            if player1_count == 6 or player2_count == 6:  # a full row
                winners.add(diagonal[0])
            elif not (diagonal[0] == diagonal[1] and diagonal[-1] == diagonal[-2]):
                if diagonal[1] == diagonal[2] and diagonal[-2] == diagonal[-3]:
                    if player1_count > player2_count:
                        winners.add(1)
                    else:
                        winners.add(2)
        diagonal = [self.get_cell(i, 4 - i) for i in range(5)]  # Small Diagonal Up
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is 5 marbles
            winners.add(diagonal[0])
        diagonal = [self.get_cell(i + 1, 5 - i) for i in range(5)]  # Small Diagonal Down
        player1_count = diagonal.count(1)
        player2_count = diagonal.count(2)
        if player1_count > 4 or player2_count > 4:  # if there is 5 marbles
            winners.add(diagonal[0])
        if len(winners) == 0:
            return -1  # no winner
        elif len(winners) == 1:
            print(winners)
            return tuple(winners)[0]  # winner
        else:
            return 0  # tie

    def state(self):
        # -1 : game continues
        #  0 : tie
        #  1 : player1 wins
        #  2 : player2 wins
        state = self.check_win()
        if state == -1:
            if self.is_filled():
                return 0  # tie
        return state


class Quarter:
    def __init__(self):
        # create an empty quarter
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def insert(self, row, column, player):
        if self.grid[row][column] == 0:
            self.grid[row][column] = player
        else:
            raise GameException("trying to inserted in a filled cell")

    def rotate(self, direction):
        """
        rotates this quarter
        1 is clockwise
        -1 is counter clockwise
        :param direction:(int) is 1 or -1 showing rotation direction
        :return: None
        """
        if type(direction) is not int:
            raise TypeError("direction should be int")
        if direction != -1 and direction != 1:
            raise ValueError("direction should be (-1 or 1)")
        for i in range(3):
            for j in range(i, 3):
                if direction == -1:
                    self.grid[i][j], self.grid[2 - j][i] = self.grid[2 - j][i], self.grid[i][j]
                elif direction == 1:
                    self.grid[i][j], self.grid[j][2 - i] = self.grid[j][2 - i], self.grid[i][j]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def get_row(self, row):
        if row < 0 or row > 2:
            raise GameException("row is between 0 and 2")
        return tuple(self.grid[row])

    def get_col(self, col):
        if col < 0 or col > 2:
            raise GameException("row is between 0 and 2")
        return tuple(self.grid[i][col] for i in range(3))

    def is_filled(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return False
        return True

    def __str__(self):
        string = ""
        for i in range(3):
            for j in range(3):
                string += str(self.grid[i][j]) + ","

        return string

    def set(self, string):
        data = string.split(',')
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = int(data[i * 3 + j])


class GameException(Exception):
    def __init__(self, msg=None):
        super(GameException, self).__init__("GameLogicException\n" + msg)
