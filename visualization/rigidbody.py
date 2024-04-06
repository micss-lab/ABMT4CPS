import math

import numpy as np
from matplotlib import pyplot as plt
from numpy import arange


class Collision:
    def __init__(self):
        # self.mass = mass
        self.velocity = 10
        # self.friction = friction
        self.gravity = -9.81
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
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        for i in range(self.steps):
            a = 0.5 * self.gravity * math.pow(i * self.interval, 2)
            b = 0.5 * self.gravity * math.pow(i * self.interval, 2)
            c = 0.5 * self.gravity * math.pow(i * self.interval, 2)

            distance_1.append(max(5, 30 + a))
            distance_2.append(max(3, 20 + b))
            distance_3.append(max(1, 10 + c))

        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3

    def plot_anylogic(self):
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        with open("../data/rigidbody_anylogic.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(abs(float(line[2:]) - 400))
                if line.startswith("2:"):
                    distance_2.append(abs(float(line[2:]) - 400))
                if line.startswith("3:"):
                    distance_3.append(abs(float(line[2:]) - 400))

        if len(distance_1) < len(distance_2):
            distance_2 = distance_2[: len(distance_1)]
        if len(distance_1) < len(distance_3):
            distance_3 = distance_3[: len(distance_1)]
        if len(distance_2) < len(distance_1):
            distance_1 = distance_1[: len(distance_2)]
        if len(distance_2) < len(distance_3):
            distance_3 = distance_3[: len(distance_2)]
        if len(distance_3) < len(distance_1):
            distance_1 = distance_1[: len(distance_3)]
        if len(distance_3) < len(distance_2):
            distance_2 = distance_2[: len(distance_3)]

        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3

    def plot_gama(self):
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        with open("../data/rigidbody_gama.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]))
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]))
                if line.startswith("3:"):
                    distance_3.append(float(line[2:]))
        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3
    def plot_mason(self):
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        with open("../data/rigidbody_mason.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(abs(float(line[2:]) - 200))
                if line.startswith("2:"):
                    distance_2.append(abs(float(line[2:]) - 200))
                if line.startswith("3:"):
                    distance_3.append(abs(float(line[2:]) - 200))
        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3
    def plot_netlogo(self):
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        with open("../data/rigidbody_netlogo.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]))
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]))
                if line.startswith("3:"):
                    distance_3.append(float(line[2:]))
        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3
    def plot_repast(self):
        distance_1 = list()
        distance_2 = list()
        distance_3 = list()
        with open("../data/rigidbody_repast.txt") as f:
            for line in f.readlines():
                if line.startswith("1:"):
                    distance_1.append(float(line[2:]) - 400)
                if line.startswith("2:"):
                    distance_2.append(float(line[2:]) - 400)
                if line.startswith("3:"):
                    distance_3.append(float(line[2:]) - 400)
        output_1 = list()
        output_2 = list()
        output_3 = list()
        for i in range(self.show):
            output_1.append(distance_1[int(len(distance_1) * (i / self.show))])
            output_2.append(distance_2[int(len(distance_2) * (i / self.show))])
            output_3.append(distance_3[int(len(distance_3) * (i / self.show))])
        return output_1, output_2, output_3
    def plot(self):
        plt.rcParams['figure.dpi'] = 1000
        plt.rcParams["figure.autolayout"] = True

        y_formula_1, y_formula_2, y_formula_3 = self.plot_formula()
        y_anylogic_1, y_anylogic_2, y_anylogic_3 = self.plot_anylogic()
        y_gama_1, y_gama_2, y_gama_3 = self.plot_gama()
        y_mason_1, y_mason_2, y_mason_3 = self.plot_mason()
        y_netlogo_1, y_netlogo_2, y_netlogo_3 = self.plot_netlogo()
        y_repast_1, y_repast_2, y_repast_3 = self.plot_repast()


        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) for x, y, z in zip(y_formula_1, y_formula_2, y_formula_3)], label="ground truth")
        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) for x, y, z in zip(y_anylogic_1, y_anylogic_2, y_anylogic_3)], alpha=0.5,
                 label="anylogic", marker="1", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) for x, y, z in zip(y_gama_1, y_gama_2, y_gama_3)], alpha=0.5, label="gama",
                 marker="_", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) / 3 for x, y, z in zip(y_mason_1, y_mason_2, y_mason_3)], alpha=0.5, label="mason",
                 marker="|", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) for x, y, z in zip(y_netlogo_1, y_netlogo_2, y_netlogo_3)], alpha=0.5, label="netlogo",
                 marker="+", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), [(abs(x - y) + abs(y - z)) for x, y, z in zip(y_repast_1, y_repast_2, y_repast_3)], alpha=0.5, label="repast",
                 marker="x", markersize=4,
                 linestyle='None')

        plt.xlabel('Step (0.01 Second)')
        plt.ylabel('Distance between 3 Objects in Y-axis')
        plt.title('Rigidbody')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    c = Collision()
    c.plot()
