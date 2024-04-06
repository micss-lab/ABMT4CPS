import math

import numpy as np
from matplotlib import pyplot as plt
from numpy import arange


class Collision:
    def __init__(self):
        self.velocity = 10
        self.steps = 1000
        self.interval = 0.01
        self.show = 100
        self.ratio = int(self.steps / self.show)
        pass

    def plot_steps(self):
        time = list()
        for i in range(self.show):
            time.append(i * self.ratio)
        return time


    def plot_formula(self):
        distance = list()
        x = 100
        y = 0
        for i in range(self.steps):
            a = x - self.velocity * self.interval * i
            b = y + self.velocity * self.interval * i
            distance.append(abs(a - b))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_anylogic(self):
        distance_1 = list()
        distance_2 = list()
        with open("../data/collision_anylogic.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]) - 350)
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]) - 350)

        if len(distance_1) < len(distance_2):
            distance_2 = distance_2[: len(distance_1)]
        elif len(distance_1) > len(distance_2):
            distance_1 = distance_1[: len(distance_2)]

        output_1 = list()
        output_2 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
        return output_1, output_2

    def plot_gama(self):
        distance_1 = list()
        distance_2 = list()
        with open("../data/collision_gama.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]))
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]))
        output_1 = list()
        output_2 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
        return output_1, output_2
    def plot_mason(self):
        distance_1 = list()
        distance_2 = list()
        with open("../data/collision_mason.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]) - 50)
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]) - 50)
        output_1 = list()
        output_2 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
        return output_1, output_2
    def plot_netlogo(self):
        distance_1 = list()
        distance_2 = list()
        with open("../data/collision_netlogo.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]))
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]))
        output_1 = list()
        output_2 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
        return output_1, output_2
    def plot_repast(self):
        distance_1 = list()
        distance_2 = list()
        with open("../data/collision_repast.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]) - 350)
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]) - 350)
        output_1 = list()
        output_2 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
        return output_1, output_2
    def plot(self):
        plt.rcParams['figure.dpi'] = 1000
        plt.rcParams["figure.autolayout"] = True

        y_anylogic_1, y_anylogic_2 = self.plot_anylogic()
        y_gama_1, y_gama_2 = self.plot_gama()
        y_mason_1, y_mason_2 = self.plot_mason()
        y_netlogo_1, y_netlogo_2 = self.plot_netlogo()
        y_repast_1, y_repast_2 = self.plot_repast()

        plt.plot(self.plot_steps(), self.plot_formula(), label="ground truth")
        plt.plot(self.plot_steps(), [abs(x - y) for x, y in zip(y_anylogic_1, y_anylogic_2)], alpha=0.5, label="anylogic", marker="1", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [abs(x - y) for x, y in zip(y_gama_1, y_gama_2)], alpha=0.5, label="gama", marker="_", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [abs(x - y) for x, y in zip(y_mason_1, y_mason_2)], alpha=0.5, label="mason", marker="|", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [abs(x - y) for x, y in zip(y_netlogo_1, y_netlogo_2)], alpha=0.5, label="netlogo", marker="+", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [abs(x - y) for x, y in zip(y_repast_1, y_repast_2)], alpha=0.5, label="repast", marker="x", markersize=4,
                 linestyle='None')


        plt.xlabel('Step (0.01 Second)')
        plt.ylabel('Distance between 2 Objects in X-axis')
        plt.title('Velocity and Collision')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    c = Collision()
    c.plot()
