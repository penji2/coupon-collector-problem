import numpy as np
import random


class Collector:

    def __init__(self, urns_amount):
        self.urns = np.zeros(urns_amount)  # list which simulates set of urns, each element of a list is an urn

    def insert_ball(self):
        while 0 in self.urns:
            test = random.randint(0, len(self.urns) - 1)  # draw an index of an urn


if __name__ == '__main__':
    urn1 = Collector(10)
    # print(urn1.urns)
    urn1.insert_ball()
