import time


class CleanerError(Exception):
    pass


class Battery20(CleanerError):
    pass


class Battery0(CleanerError):
    pass


class WaterError(CleanerError):
    pass


class TrashError(CleanerError):
    pass


class VacuumCleaner:
    def __init__(self):
        self.level_battery = 100
        self.level_trash = 0
        self.level_water = 5

    def move(self):
        while True:
            try:
                if self.level_battery <= 2:
                    raise Battery0()
                elif self.level_battery <= 20:
                    raise Battery20()
                VacuumCleaner.wash(self)
                VacuumCleaner.vacuum_cleaner(self)
                time.sleep(1)
            except Battery0:
                print('Goodbye............')
                break
            except Battery20:
                print('Boss i need your help. Charge me')
                if self.level_water or self.level_trash:
                    print('Full of trash and no water')
                    break

    def wash(self):
        try:
            if self.level_water <= 1:
                print('Running out of water')
            elif self.level_water == 0:
                return WaterError()
            print('-Washing-')
            self.level_battery -= round(self.level_battery * 0.2)
            self.level_water -= 1
            print(f'Level baterry: {self.level_battery} Level water: {self.level_water}')
        except WaterError:
            return False

    def vacuum_cleaner(self):
        try:
            if self.level_trash == 4:
                return TrashError()
            elif self.level_trash == 3:
                print('Stop bro enough')
            print('-Cleaning-')
            self.level_battery -= round(self.level_battery * 0.2)
            self.level_trash += 1
            print(f'Level baterry: {self.level_battery} Trash level:'
                  f' {self.level_trash} ')
        except TrashError:
            return False


c = VacuumCleaner()
c.move()
