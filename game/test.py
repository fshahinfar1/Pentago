# test game state function
import game.board

b = game.board.Board()
# column test
# b.insert(0, 0, 1)
# b.insert(1, 0, 1)
# b.insert(2, 0, 1)
# b.insert(3, 0, 1)
# b.insert(4, 0, 1)
# print(b.state, 1)

# column test
# b.insert(0, 5, 1)
# b.insert(2, 5, 1)
# b.insert(3, 5, 1)
# b.insert(4, 5, 1)
# b.insert(5, 5, 1)
# print(b.state())

# row test
# b.insert(0, 0, 1)
# b.insert(0, 1, 1)
# b.insert(0, 2, 1)
# b.insert(0, 3, 1)
# b.insert(0, 4, 1)
# print(b.state())

# row test
# b.insert(0, 0, 1)
# b.insert(0, 1, 1)
# b.insert(0, 2, 1)
# b.insert(0, 3, 1)
# b.insert(0, 4, 1)
# b.insert(0, 5, 1)
# print(b.state())

# big diagonal test
# b.insert(0, 0, 2)
# b.insert(1, 1, 1)
# b.insert(2, 2, 1)
# b.insert(3, 3, 1)
# b.insert(4, 4, 1)
# b.insert(5, 5, 1)
# print(b.state())

# big diagonal test
# b.insert(0, 0, 1)
# b.insert(1, 1, 1)
# b.insert(2, 2, 1)
# b.insert(3, 3, 2)
# b.insert(4, 4, 1)
# b.insert(5, 5, 1)
# print(b.state())

# tie test
# b.insert(0, 0, 1)
# b.insert(0, 1, 1)
# b.insert(0, 2, 1)
# b.insert(0, 3, 1)
# b.insert(0, 4, 1)
# b.insert(0, 5, 2)
# b.insert(1, 4, 2)
# b.insert(2, 3, 2)
# b.insert(3, 2, 2)
# b.insert(4, 1, 2)
# print(b.state())

