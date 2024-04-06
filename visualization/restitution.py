import math

import numpy as np
from matplotlib import pyplot as plt
from numpy import arange


class Collision:
    def __init__(self):
        self.gravity = -9.81
        self.steps = 1000
        self.interval = 0.01
        self.restitution = 1
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
        y = 100
        v = 0
        t = 0
        while t < 10:
            y += v * 0.01
            if y > 0:
                v += self.gravity * self.interval
            else:
                v = -self.restitution * v  # bounce off floor with Coefficient of restitution - COR
            distance.append(y)
            t += 0.01
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_anylogic(self):
        distance = list()
        with open("../data/gravity_anylogic.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_gama(self):
        distance = list()
        with open("../data/restitution_gama.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_mason(self):
        distance = list()
        with open("../data/restitution_mason.txt") as f:
            for line in f.readlines():
                distance.append(abs(float(line) - 187))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_netlogo(self):
        distance = list()
        with open("../data/gravity_netlogo.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_repast(self):
        distance = list()
        with open("../data/gravity_repast.txt") as f:
            for line in f.readlines():
                distance.append(abs(float(line) - 400))
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
        plt.ylabel('Y-axis Position in Simulation Space')
        plt.title('Restitution')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    c = Collision()
    c.plot()
