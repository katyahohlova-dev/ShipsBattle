import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self.length = length
        self.x = x #координаты начала
        self.y = y
        self.is_move = True #передвижение двигаться
        self.cells = [1 for i in range(self.length)] #попадание, в какую-нибудь из палуб корабля (1 - попадание не было, 2 - попадание было)
        self.tp = tp

    def get_start_coords(self):
        return self.x, self.y

    def place_ship(self): #размещение корабля на игровом поле с проверкой

        pass #на выход за пределы границы и соприкосновение с другими кораблями


class Field:
    def __init__(self, size=10, shots=None):
        self.size = size
        self.pole = []
        self.shots = shots #матрица для отслеживания выстрелов (попадание/промах)
        self.ships = [] #список из короблей, которые будут отображаться на поле

    def show_pole(self):
        for row in self.pole:
            for ship in row:
                print('*' if ship else '.', end=' ')
            print()

    def init(self): #начальная инициализация игрового поля
        pass #здесь же создается список из кораблей

    def get_ships(self):
        pass

    def init(self) -> None:
        self.pole = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for length in range(1, 5):
            count = 5 - length
            for _ in range(count):
                self.ships.append(Ship(length, random.randint(1, 2)))

        while self.ships:
            obj = self.ships.pop()

            obj.x = random.randint(0, self.size-1)
            obj.y = random.randint(0, self.size-1)

            if obj.tp == 1:  #горизонт
                if obj.x + obj.length > self.size:
                    continue

                for x in range(max(0, obj.x-1), min(self.size, obj.x+2)):
                    for y in range(max(0, obj.y-1), min(self.size, obj.y+2)):
                        if self.pole[x][y] != 0:
                            conflict = True
                            break
                if conflict:
                    continue

                for i in range(obj.length - 1):
                    self.pole[obj.y][obj.x + i] = obj

            elif obj.tp == 2:
                if obj.y + obj.length > self.size:
                    continue

                conflict = False
                for i in range(obj.length - 1):
                    if self.pole[obj.y][obj.x + i] != 0 or self.pole[obj.y + i][obj.x + i] != 0 or self.pole[obj.y][
                        obj.x - i] != 0 or self.pole[obj.y - i][obj.x + i]:
                        conflict = True
                        break
                if conflict:
                    continue


                for j in range(obj.length-1):
                    self.pole[obj.y + j][obj.x] = obj



    def initialize(self, obj: Ship): #метод для инициализации игрового поля и размещения кораблей
            obj.x = random.randint(0, self.size)
            obj.y = random.randint(0, self.size)

            if obj.tp == 1: #горизонтальное расположение
                if obj.x + obj.length > self.size:
                    raise ValueError('Корабль выходит за границы поля по горизонтали')
                for i in range(obj.length):
                    self.pole[obj.y][obj.x+i] = obj
            elif obj.tp == 2:
                if obj.y + obj.length > self.size:
                    raise ValueError('Корабль выходит за границы поля по вертикали')
                for j in range(obj.length):
                    self.pole[obj.y+j][obj.x] = obj

    def add_ship(self, ship):
        pass

    #def check_hint(self, x, y):
    #    if self.field[x][y] == '#': #метод для проверки, попал ли выстрел в корабль
    #        self.shots.get((x,y), '#')

    def record_shot(self): pass #метод для записи результата выстрела

    def check_win(self): pass #метод для проверки, остались ли ещё корабли на поле

class SeaBattle:
    def __init__(self): pass

    def main(self):
        x = input('Введите координату x для выстрела: ')
        y = input('Введите координату y для выстрела: ')

        #self.check_hint(x, y)


# y = 3
# length = 4
# for j in range(y, y + length+1):
#     print(j, end=" ")
field  = Field()
field.init()
field.show_pole()
#ship1 = Ship(3, 1, 4, 3)
#field.initialize(ship1)
#field.show_pole()






