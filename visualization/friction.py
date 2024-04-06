import math

import numpy as np
from matplotlib import pyplot as plt
from numpy import arange


class Collision:
    def __init__(self):
        # self.mass = mass
        self.velocity = 10
        self.friction = 1
        self.gravity = 9.81
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
        for i in range(self.steps):
            x = pow(self.velocity, 2) / (2 * self.friction * self.gravity) * (self.interval * i)
            distance.append(x)

        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_anylogic(self):
        distance = list()
        with open("../data/friction_anylogic.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_gama(self):
        distance = list()
        with open("../data/friction_gama.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_mason(self):
        distance = list()
        with open("../data/friction_mason.txt") as f:
            for line in f.readlines():
                distance.append(float(line) - 15)
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_netlogo(self):
        distance = list()
        with open("../data/friction_netlogo.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_repast(self):
        distance = list()
        with open("../data/friction_repast.txt") as f:
            for line in f.readlines():
                distance.append(abs(float(line) - 450))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot(self):
        plt.rcParams['figure.dpi'] = 1000
        plt.rcParams["figure.autolayout"] = True

        plt.plot(self.plot_steps(), self.plot_formula(), label="ground truth")
        plt.plot(self.plot_steps(), self.plot_anylogic(), alpha=0.5, label="anylogic", marker="1", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), self.plot_gama(), alpha=0.5, label="gama", marker="_", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), self.plot_mason(), alpha=0.5, label="mason", marker="|", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), self.plot_netlogo(), alpha=0.5, label="netlogo", marker="+", markersize=4,
                 linestyle='None')
        plt.plot(self.plot_steps(), self.plot_repast(), alpha=0.5, label="repast", marker="x", markersize=4,
                 linestyle='None')

        plt.xlabel('Step (0.01 Second)')
        plt.ylabel('X-axis Position in Simulation Space')
        plt.title('Friction')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    c = Collision()
    c.plot()
