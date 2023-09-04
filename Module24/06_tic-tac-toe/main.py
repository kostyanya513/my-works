class Cell:
    condition = ['-', 'O', 'X']

    def __init__(self, number):
        self.number = number


class Board:
    cells = [
        Cell.condition[0], Cell.condition[0], Cell.condition[0],
        Cell.condition[0], Cell.condition[0], Cell.condition[0],
        Cell.condition[0], Cell.condition[0], Cell.condition[0]
    ]


class Player:
    name1 = 'Крестик'
    name2 = 'Нолик'

    def step_1(self):
        print('На какую клетку ходит {}?'.format(Player.name1))
        step_1 = int(input())
        Game.step_1(self, step_1)

    def step_2(self):
        print('На какую клетку ходит {}?'.format(Player.name2))
        step_2 = int(input())
        Game.step_2(self, step_2)


class Game:
    def __init__(self):
        self.play = 0
        self.viktory1 = 0
        self.viktory2 = 0

    #
    def new_play(self):
        while True:
            print('Начнем игру?')
            start = int(input('1 - Да; 2 - Нет: '))
            if start == 1:
                print('Играем!')
                self.start_game()
                self.game_score()
            elif start == 2:
                print('Не играем')
                break
            else:
                print('Неправильная команда!')

    def start_game(self):
        print('Очищаем поле!')
        Game.clear_field(self)

    def first_move(self):
        self.play += 1
        begin = int(input('Кто начинает? 1 (играет за крестики) или 2 (играет за нолики): '))
        if begin == 1:
            Player.step_1(self)
        elif begin == 2:
            Player.step_2(self)
        else:
            print('Нет такого игрока!')

    def game_score(self):
        print('Количество игр: {}, Побед Крестика: {}, Побед Нолика: {}'.format(
            self.play,
            self.viktory1,
            self.viktory2,
        ))

    def hod1(self, number):
        one_move = True
        game = True
        while one_move:
            if Board.cells[number - 1] == Cell.condition[0]:
                Board.cells[number - 1] = Cell.condition[2]
                print('Поле игры')
                print('{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}'.format(
                    Board.cells[0],
                    Board.cells[1],
                    Board.cells[2],
                    Board.cells[3],
                    Board.cells[4],
                    Board.cells[5],
                    Board.cells[6],
                    Board.cells[7],
                    Board.cells[8])
                )
                if self.proverka(Board.cells, 'X'):
                    print('Крестик победил!')
                    self.viktory1 += 1
                    break
                if Board.cells.count('-') == 0:
                    game = False
                    break
                Player.step_2(self)
                break
            else:
                print('Клетка занята! Выбери другую.')
                number = int(input('Ваш ход: '))
        if not game:
            print('Стоп игра!')

    def hod2(self, number):
        one_move = True
        game = True
        while one_move:
            if Board.cells[number - 1] == Cell.condition[0]:
                Board.cells[number - 1] = Cell.condition[1]
                print('Поле игры')
                print('{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}'.format(
                    Board.cells[0],
                    Board.cells[1],
                    Board.cells[2],
                    Board.cells[3],
                    Board.cells[4],
                    Board.cells[5],
                    Board.cells[6],
                    Board.cells[7],
                    Board.cells[8])
                )
                if self.proverka(Board.cells, 'O'):
                    print('Нолик победил!')
                    self.viktory2 += 1
                    break
                if Board.cells.count('-') == 0:
                    game = False
                    break
                Player.step_1(self)
                break
            else:
                print('Клетка занята! Выбери другую.')
                number = int(input('Ваш ход: '))
        if not game:
            print('Стоп игра!')

    def proverka(self, cells, number):
        if (cells[0] == number and cells[3] == number and cells[6] == number) \
                or (cells[1] == number and cells[4] == number and cells[7] == number) \
                or (cells[2] == number and cells[5] == number and cells[8] == number) \
                or (cells[0] == number and cells[1] == number and cells[2] == number) \
                or (cells[3] == number and cells[4] == number and cells[5] == number) \
                or (cells[6] == number and cells[7] == number and cells[8] == number) \
                or (cells[0] == number and cells[4] == number and cells[8] == number) \
                or (cells[2] == number and cells[4] == number and cells[6] == number):
            print('Победа!')
            return True
        else:
            return False

    def clear_field(self):
        Board.cells = [Cell.condition[0] for _ in range(9)]

        print('{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}'.format(
            Board.cells[0],
            Board.cells[1],
            Board.cells[2],
            Board.cells[3],
            Board.cells[4],
            Board.cells[5],
            Board.cells[6],
            Board.cells[7],
            Board.cells[8])
        )
        self.first_move()


play = Game()
play.new_play()
