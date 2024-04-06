import math

from matplotlib import pyplot as plt


class Gravity:
    def __init__(self):
        self.gravity = -9.81
        self.steps = 1000
        self.interval = 0.01
        self.show = 100
        self.ratio = int(self.steps / self.show)

    def plot_steps(self):
        time = list()
        for i in range(self.show):
            time.append(i * self.ratio)
        return time

    def plot_formula(self):
        distance = list()
        for i in range(self.show):
            x = 0.5 * self.gravity * math.pow(i * self.interval * self.ratio, 2)
            distance.append(max(0, int(100 + x)))
        return distance

    def plot_anylogic(self):
        distance = list()
        with open("../data/gravity_anylogic.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_gama(self,):
        distance = list()
        with open("../data/gravity_gama.txt") as f:
            for line in f.readlines():
                distance.append(float(line))
        output = list()
        for i in range(self.show):
            output.append(distance[int(len(distance) * (i / self.show))])
        return output

    def plot_mason(self):
        distance = list()
        with open("../data/gravity_mason.txt") as f:
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
        plt.plot(self.plot_steps(), self.plot_anylogic(), alpha=0.5, label="anylogic", marker="1", markersize=4, linestyle='None')
        plt.plot(self.plot_steps(), self.plot_gama(), alpha=0.5, label="gama", marker="_", markersize=4, linestyle='None')
        plt.plot(self.plot_steps(), self.plot_mason(), alpha=0.5, label="mason", marker="|", markersize=4, linestyle='None')
        plt.plot(self.plot_steps(), self.plot_netlogo(), alpha=0.5, label="netlogo", marker="+", markersize=4, linestyle='None')
        plt.plot(self.plot_steps(), self.plot_repast(), alpha=0.5, label="repast", marker="x", markersize=4, linestyle='None')

        plt.xlim(right=500)
        plt.xlabel('Step (0.01 Second)')
        plt.ylabel('Y-axis Position in Simulation Space')
        plt.title('Gravity')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    c = Gravity()
    c.plot()
