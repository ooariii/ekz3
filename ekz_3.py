class Tomato:
    states = {0: 'ничего', 1: 'росток', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._sl_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

class Tomatobush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Он еще работает')
        self._plant.grow_all()
        print('Он закончил')

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('все ок')
        else:
            print('рано еще собирать')

    @staticmethod
    def knowledge_base(self):
        print('справка по садоводству ;)))')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(3)
    gardener = Gardener('имя', great_tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()