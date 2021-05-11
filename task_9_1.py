import time
import itertools


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 10}

    def running(self):
        for i in itertools.cycle(self.__color):
            print(f'\r{i}', end='')
            time.sleep(self.__color.get(i))


trafficlight = TrafficLight()
trafficlight.running()
