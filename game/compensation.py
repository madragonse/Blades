


import math
from typing import List
from timeit import default_timer as timer


MAX_E_MUL = 4.0
class Compensation():
    def __init__(self):
        self.last = [0, 0]

        self.data_tendention = []
        self.last_eclaption = 1

        self.data_predicted = None
        self.timer_eclaption_begining = timer()
        self.timer_last = timer()
        
        self.max_eclapse = 1



        
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
 
            intensivity = self.intensity_function_cos(timer() - self.timer_eclaption_begining, 1 + self.last_eclaption)

            for i in range(0, len(self.last_ret)):
                self.last_ret[i] += self.data_tendention[i]*intensivity
        else:
            if self.last == []:
                self.last_eclaption = timer() - self.timer_eclaption_begining
                self.timer_eclaption_begining = 0
                self.data_tendention = []
                for e in input:
                    self.data_tendention.append(0)
            else:
                self.data_tendention = []
                for i in range(0, len(input)):
                    self.data_tendention.append(input[i] - self.last[i])
            self.last_ret = input

        print(self.data_tendention)
        self.last = input
        
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
