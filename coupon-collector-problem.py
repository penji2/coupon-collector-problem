import numpy as np
import random
import matplotlib.pyplot as plt


class Collector:

    def __init__(self, urns_amount, exp_amount):
        self.urns = np.zeros(urns_amount)  # list which simulates set of urns, each element of a list is an urn
        self.exp_amount = exp_amount

    def insert_ball(self):
        guard = 1
        count_empty = 0   # counts number of balls needed to fill all urns
        count_2balls = 0  # counts number of balls needed to fill at least 1 urn with 2 balls
        while 0 in self.urns:
            index = random.randint(0, len(self.urns) - 1)  # draw an index of an urn
            self.urns[index] += 1
            count_empty += 1
            if guard:
                count_2balls += 1
            if 2 in self.urns:
                guard = 0
        #  print("Number of balls in each urn at the end:", len(self.urns), "urns", self.urns)
        return count_empty, count_2balls

    def averaging(self):
        avr_count_empty = 0
        avr_count_2balls = 0

        for i in range(self.exp_amount):
            count_tuple = self.insert_ball()

            avr_count_empty += count_tuple[0]
            avr_count_2balls += count_tuple[1]

            self.urns = np.zeros(len(self.urns))  # making zeros list again for averaging purpose

        avr_count_empty /= self.exp_amount
        avr_count_2balls /= self.exp_amount

        return avr_count_empty, avr_count_2balls


class Main:

    @staticmethod
    def get_data_for_plot(obj_list, start, stop, step):
        x, y1, y2 = list(), list(), list()
        for i in obj_list:
            y1.append(i.averaging()[0])
            y2.append(i.averaging()[1])

        x = [i for i in range(start, stop, step)]
        return x, y1, y2

    @staticmethod
    def plot_avr(obj_list, start, stop, step):
        x, y1, y2 = Main.get_data_for_plot(obj_list, start, stop, step)
        label_font_size = 20

        f1 = plt.figure(1)
        plt.plot(x, y1, 'o')
        plt.title("Every urn filled with at least 1 ball", fontsize=label_font_size)
        plt.xlabel("n", fontsize=label_font_size)
        plt.ylabel("Amount of balls", fontsize=label_font_size)

        f2 = plt.figure(2)
        plt.plot(x, y2, 'o')
        plt.title("At least 1 urn with 2 balls", fontsize=label_font_size)
        plt.xlabel("n", fontsize=label_font_size)
        plt.ylabel("Amount of balls", fontsize=label_font_size)
        plt.show()


if __name__ == '__main__':
    urn = list()
    start = 10
    stop = 500
    step = 10
    exp_amount = 500
    for i in range(start, stop, step):
        urn.append(Collector(i, exp_amount))
    Main.plot_avr(urn, start, stop, step)

    print("Average number of balls needed to fill every urn:", urn[0].averaging()[0])
    print("and average number of balls needed to fill at least 1 urn with 2 balls:", urn[0].averaging()[1], "for 10 urns")