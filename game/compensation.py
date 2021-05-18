


import math
from typing import List
from timeit import default_timer as timer
from copy import copy, deepcopy

MAX_E_MUL = 4.0
class Compensation():
    def __init__(self):
        self.last = []
        self.last_ret = []
        self.last_real = []

        self.data_tendention = []
        self.last_eclaption = 1.0

        self.data_predicted = None
        self.timer_eclaption_begining = timer()
        self.timer_last = timer()
        
        self.max_eclapse = 1.0
        self.cum_time = 0.0



        
    def intensity_function_cos(self, time:float, max_eclapse) -> float:
        f_range = math.pi / 2
        max = max_eclapse * f_range
        if time >= max:
            return 0
        else:
            return math.cos(time)
    

    def input(self, input:List):
        stoper = timer()
        deltatime = stoper - self.timer_last
        self.timer_last = stoper
        if input == []:
            if input == self.last:
                pass
            else:
                self.timer_eclaption_begining = timer()
            if self.cum_time + deltatime > 0.05:
                #print(self.data_tendention)
                intensivity = self.intensity_function_cos(timer() - self.timer_eclaption_begining, 1 + self.last_eclaption)
                intensivity = 1
                for i in range(0, len(self.data_tendention)):
                    self.last_ret[i] += self.data_tendention[i]*intensivity*deltatime
            else:
                self.cum_time += deltatime
                # self.last_ret = copy(input)
                self.last = copy(input)
                return input
        else:
            self.cum_time = 0
            if self.last == []:
                self.last_eclaption = timer() - self.timer_eclaption_begining
                self.data_tendention = []
                for i in range(0, len(self.last_real)):
                    self.data_tendention.append((input[i] - self.last_real[i])/self.last_eclaption)
            else:
                self.data_tendention = []
                for i in range(0, len(input)):
                    self.data_tendention.append((input[i] - self.last_ret[i])/deltatime)
            self.timer_eclaption_begining = timer()

            self.last_real = []
            for e in input:
                self.last_real.append(e)
            self.last_ret = copy(input)

        self.last = copy(input)
        

        return self.last_ret


# import time

# com1 = Compensation()

# print(com1.input([1, 2]))
# print(com1.input([2, 3]))
# print(com1.input([3, 4]))

# print(com1.input([]))
# time.sleep(0.4)
# print(com1.input([]))
# time.sleep(0.4)
# print(com1.input([]))
# time.sleep(0.4)
# print(com1.input([]))

# print(com1.input([3, 4]))
# print(com1.input([2, 4]))
# print(com1.input([3, 4]))
