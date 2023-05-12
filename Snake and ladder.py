import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

class Board:
    def __init__(self, size, ladders, snakes):
        self.size = size
        self.ladders = ladders
        self.snakes = snakes

    def move(self, player, steps):
        new_position = player.position + steps
        if new_position <= self.size:
            player.position = new_position
            if player.position in self.ladders:
                player.position = self.ladders[player.position]
                print(f"{player.name} climbed a ladder!")
            elif player.position in self.snakes:
                player.position = self.snakes[player.position]
                print(f"{player.name} got bitten by a snake!")
        else:
            print(f"{player.name} rolled too high and cannot move.")

class Game:
    def __init__(self, num_players, final_square):
        self.num_players = num_players
        self.final_square = final_square
        self.players = []
        self.board = Board(final_square, {2: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100},
                           {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78})

    def setup_players(self):
        for i in range(self.num_players):
            name = input(f"Enter the name of player {i+1}: ")
            player = Player(name)
            self.players.append(player)

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        current_player_index = 0

        while True:
            current_player = self.players[current_player_index]

            input(f"{current_player.name}, press Enter to roll the dice...")
            dice_roll = self.roll_dice()

            print(f"{current_player.name} rolled a {dice_roll}.")
            self.board.move(current_player, dice_roll)

            print(f"{current_player.name} is now at square {current_player.position}.\n")

            if current_player.position >= self.final_square:
                print(f"{current_player.name} wins!")
                break

            current_player_index = (current_player_index + 1) % self.num_players

# Main code execution
num_players = int(input("Enter the number of players: "))
final_square = 100

game = Game(num_players, final_square)
game.setup_players()
game.play()
