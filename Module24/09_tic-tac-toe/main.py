class Board:
    def __init__(self):
        self.board = {str(i): i for i in range(1, 10)}
        self.player_list = list()
        for i in range(1, 3):
            if len(self.player_list) == 0:
                self.player_list.append(Player())
            else:
                self.player_list.append(Player(self.player_list[0].simbol))

    def players_info(self):
        for i in range(len(self.player_list)):
            print('{}) игрок'.format(i+1))
            self.player_list[i].player_info()

    def motion(self, index):
        print('На какую клетку вы хотите поставить {}(от 1 до 9 например 5)?'.format(self.player_list[index].simbol))
        while True:
            move = input()
            if self.board[move] != 'X' and self.board[move] != 'O':
                self.board[move] = self.player_list[index].simbol
                break
            else:
                self.print_board()
                print('Клетка занята!Попробуйте еще раз')

    def print_board(self):
        print('{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}'.format(self.board['1'], self.board['2'], self.board['3'],
                                                          self.board['4'], self.board['5'], self.board['6'],
                                                          self.board['7'], self.board['8'], self.board['9']))

    def win_board_check(self):
        if self.win_line_check('1', '2', '3') is True or self.win_line_check('4', '5', '6') is True \
                or self.win_line_check('7', '8', '9') is True or self.win_line_check('1', '4', '7') is True \
                or self.win_line_check('2', '5', '8') is True or self.win_line_check('3', '6', '9') is True \
                or self.win_line_check('1', '5', '9') is True or self.win_line_check('7', '5', '3') is True:
            return True

    def win_line_check(self, one, two, three):
        if self.board[one] == self.board[two] and self.board[two] == self.board[three]:
            return True
        else:
            return False


class Player:
    def __init__(self, simbol='Пусто'):
        self.name = input('Введите имя игрока: ')
        if simbol.lower() == 'x' or simbol.lower() == 'х':
            self.simbol = 'O'
        elif simbol.lower() == 'o' or simbol.lower() == 'о' or simbol.lower == '0':
            self.simbol = 'X'
        else:
            while True:
                question = input('Крестик или нолик ? (X/O) ').lower()
                if question == 'x' or question == 'х':
                    self.simbol = 'X'
                    break
                elif question == 'o' or question == 'о' or question == '0':
                    self.simbol = 'O'
                    break
                else:
                    print('Выберите: ')

    def player_info(self):
        print('Имя {}\nСимвол {}\n'.format(self.name, self.simbol))


board_1 = Board()
board_1.players_info()
count = 0
while True:
    board_1.motion(0)
    board_1.print_board()
    if board_1.win_board_check():
        print('Победил {}'.format(board_1.player_list[0].name))
        break
    board_1.motion(1)
    board_1.print_board()
    if board_1.win_board_check():
        print('Победил {}'.format(board_1.player_list[1].name))
        break
    count += 1
    if count == 9:
        print('Ничья!')
        break
