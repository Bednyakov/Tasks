class Cell:
    title = 'Клетка'
    def __init__(self, index, busy=False):
        self.index = index
        self.busy = busy

class Player:
    title = 'Игрок'
    __num_player = 0
    def __init__(self):
        Player.__num_player += 1
        if Player.__num_player < 2:
            self.index = 'X'
        else:
            self.index = 'O'

class Board:
    title = 'Доска'
    cell1 = Cell('1')
    cell2 = Cell('2')
    cell3 = Cell('3')
    cell4 = Cell('4')
    cell5 = Cell('5')
    cell6 = Cell('6')
    cell7 = Cell('7')
    cell8 = Cell('8')
    cell9 = Cell('9')
    cellset = (cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9)

class Game:
    title = 'Игра'

    count = 0
    p1 = Player()
    p2 = Player()
    board1 = Board()

    winline1 = (Board.cellset[0], Board.cellset[1], Board.cellset[2])
    winline2 = (Board.cellset[3], Board.cellset[4], Board.cellset[5])
    winline3 = (Board.cellset[6], Board.cellset[7], Board.cellset[8])
    winline4 = (Board.cellset[0], Board.cellset[4], Board.cellset[8])
    winline5 = (Board.cellset[2], Board.cellset[4], Board.cellset[6])
    winline6 = (Board.cellset[0], Board.cellset[3], Board.cellset[6])
    winline7 = (Board.cellset[1], Board.cellset[4], Board.cellset[7])
    winline8 = (Board.cellset[2], Board.cellset[5], Board.cellset[8])
    winset = (winline1, winline2, winline3, winline4, winline5, winline6, winline7, winline8)

    def finish(self, winset):
        buscount = 0
        for set in winset:
            if set[0].busy == True and set[1].busy == True and set[2].busy == True:
                if set[0].index == set[1].index and set[0].index == set[2].index:
                    print(f'Победа игрока {set[0].index}!')
                    return True
        for i in Board.cellset:
            if i.busy == True:
                buscount += 1
                if buscount == 9:
                    print(f'Ничья!')
                    return True

    def start(self):
        self.fin = False
        while True:
            self.fin = self.finish(self.winset)
            if self.fin == True:
                break
            print(f'Игрок {self.p1.index}, ', end='')
            move_p1 = int(input('введите индекс клетки для хода: '))
            if Board.cellset[move_p1 - 1].busy == False:
                Board.cellset[move_p1 - 1].index = self.p1.index
                Board.cellset[move_p1 - 1].busy = True
                self.gameinfo()
            else:
                print('Пропуск хода...')

            self.fin = self.finish(self.winset)
            if self.fin == True:
                break
            print(f'Игрок {self.p2.index}, ', end='')
            move_p2 = int(input('введите индекс клетки для хода: '))
            if Board.cellset[move_p2 - 1].busy == False:
                Board.cellset[move_p2 - 1].index = self.p2.index
                Board.cellset[move_p2 - 1].busy = True
                self.gameinfo()
            else:
                print('Пропуск хода...')

    def gameinfo(self):
        self.count += 1
        if self.count == 1:
            print('\tДобро пожаловать в игру "крестики-нолики"!')
        print(f'''
\t\t\t\t[{Board.cellset[0].index}] [{Board.cellset[1].index}] [{Board.cellset[2].index}]
\t\t\t\t[{Board.cellset[3].index}] [{Board.cellset[4].index}] [{Board.cellset[5].index}]
\t\t\t\t[{Board.cellset[6].index}] [{Board.cellset[7].index}] [{Board.cellset[8].index}]''')

game = Game()
game.gameinfo()
game.start()
