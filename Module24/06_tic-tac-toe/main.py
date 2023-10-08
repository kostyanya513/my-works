class Cell:
    condition = ['X', '0', 'Свободна']


class Board:
    cells = [Cell.condition[2] for _ in range(1, 10)]

    def print_board(self):
        print(self.cells)


class Player:
    def __init__(self, name):
        self.name = name

    def hod_player(self):
        print('{}'.format(self.name), end=' ')
        hod = int(input('ходит на клетку: '))
        return hod


class Game:
    def __init__(self, cell):
        self.players = []
        self.cell = cell
        self.count = 0
        self.count_1 = 0
        self.count_2 = 0

    def add_player(self, player):
        self.players.append(player)

    @staticmethod
    def proverka(cells, cond_cell):
        if (cells[0] == cond_cell and cells[3] == cond_cell and cells[6] == cond_cell) \
                or (cells[1] == cond_cell and cells[4] == cond_cell and cells[7] == cond_cell) \
                or (cells[2] == cond_cell and cells[5] == cond_cell and cells[8] == cond_cell) \
                or (cells[0] == cond_cell and cells[1] == cond_cell and cells[2] == cond_cell) \
                or (cells[3] == cond_cell and cells[4] == cond_cell and cells[5] == cond_cell) \
                or (cells[6] == cond_cell and cells[7] == cond_cell and cells[8] == cond_cell) \
                or (cells[0] == cond_cell and cells[4] == cond_cell and cells[8] == cond_cell) \
                or (cells[2] == cond_cell and cells[4] == cond_cell and cells[6] == cond_cell):
            return True

    def count_play(self, name_player):
        if name_player == self.players[0].name:
            self.count_1 += 1
        else:
            self.count_2 += 1

    def move(self, who):
        while True:
            if who == self.players[0].name:
                if self.one_move(self.players[0], Cell.condition[0]):
                    return True
                else:
                    self.one_move(self.players[1], Cell.condition[1])
            elif who == self.players[1].name:
                if self.one_move(self.players[1], Cell.condition[1]):
                    return True
                else:
                    self.one_move(self.players[0], Cell.condition[0])

    def one_move(self, player, cond):
        index_cell = player.hod_player() - 1
        while True:
            if self.cell.cells[index_cell] != Cell.condition[2]:
                print('Клетка занята! Выбери другую.')
                index_cell = player.hod_player() - 1
            else:
                self.cell.cells[index_cell] = cond
                break
        print(self.cell.cells)
        if self.proverka(self.cell.cells, cond):
            print('Победил {}'.format(player.name))
            self.count_play(player.name)
            return True
        else:
            return False

    def play(self):
        self.cell.cells = [Cell.condition[2] for _ in range(9)]
        print(self.cell.cells)
        for _ in range(9):
            print('Кто ходит? {} или {}?'.format(self.players[0].name, self.players[1].name), end=' ')
            whose_move = input()
            if self.move(whose_move):
                print('Игра завершена!')
                return True
        print('Ничья!')

    def new_play(self):
        print('Играют два игрока: {} и {}'.format(self.players[0].name, self.players[1].name))
        self.play()
        self.count += 1
        while True:
            next_play = input('Продолжаем играть? (Да/Нет): ')
            if next_play.lower() == 'да':
                self.play()
                self.count += 1
            elif next_play.lower() == 'нет':
                print('Игр {}; {} победил {} раз; {} победил {} раз'.format(
                    self.count,
                    self.players[0].name,
                    self.count_1,
                    self.players[1].name,
                    self.count_2
                ))
                break
            else:
                print('Неизвестная команда! Повторите ввод.')


board = Board()
player_1 = Player('Кот')
player_2 = Player('Пес')
game = Game(board)
game.add_player(player_1)
game.add_player(player_2)
game.new_play()
