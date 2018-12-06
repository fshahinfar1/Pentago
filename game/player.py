"""
Farbod Shahinfar
Pentago Game

"""


class Player:
    player_count = 1

    def __init__(self, is_turn):
        self.is_turn = is_turn
        self.player_number = Player.player_count
        Player.player_count += 1
        self.marbles = 0

    def your_turn(self):
        print("it is player number %d turn\nplease place your marble and give quarter with rotation direction"
              % self.player_number)
        # enter "row column quarter direction"
        t = ()
        while True:
            try:
                t = tuple(int(x) for x in input().split())
                if len(t) != 4:
                    raise ValueError
                if t[0] < 0 or t[0] > 5:
                    raise ValueError
                if t[1] < 0 or t[1] > 5:
                    raise ValueError
                if t[2] < 0 or t[2] > 3:
                    raise ValueError
                if t[3] != -1 and t[3] != 1:
                    raise ValueError
                break
            except ValueError:
                print("please enter correct values:")
                print("row column quarter direction")
        return t
