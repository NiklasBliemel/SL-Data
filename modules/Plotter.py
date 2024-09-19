import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class Plotter:
    def __init__(self):
        self.mu_o = 4 * np.pi * 1e-7
        self.l_ext = 15.8 * 1e-2
        self.N_ext = 6245
        self.I_const = 8e-6
        self.I_ht_const = 1.95 * 1e-3

    def model_function(self, x, B_C, T_C):
        return B_C * (1 - (x / T_C) ** 2)

    def B_function(self, x):
        return (self.mu_o * x * self.N_ext) / self.l_ext

    def R1_function(self, x):
        return x * 3e-3 / self.I_const

    def R2_function(self, x):
        return x * 1e-2 / self.I_const

    def R3_function(self, x):
        return (x / self.I_ht_const) * 1e3

    def T_function(self, x):
        return np.sqrt((x * 1e6)/0.0637 + 16111) - 49.5

    def n_function(self, x):
        return x

    def plot_with_fit(self, data=np.array([[0, 0]]), x_label="x - Axis", y_label="y - Axis", title="Plot Title"):
        fig, ax = plt.subplots()
        ax.set_title(title, fontsize=16, pad=15)
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True)

        x_data = data[:, 0]
        y_data = self.B_function(data[:, 1])

        ax.plot(x_data, y_data, color='black', linestyle="", marker='o', markersize=5)

        popt, pcov = curve_fit(self.model_function, x_data, y_data, p0=[1, 1])

        x_fit = np.linspace(0, max(x_data), 1000)
        y_fit = self.model_function(x_fit, *popt)

        ax.plot(x_fit, y_fit, color='red', linestyle="-", label=r"$B_c(T)\left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]$")
        ax.legend(loc='best', draggable=True)

        print(popt, np.diag(pcov))

        plt.show()

    def plot(self, data=np.array([[0, 0]]), vline=None, hline=None, x_label="x - Axis", y_label="y - Axis", title="Plot Title"):
        fig, ax = plt.subplots()
        ax.set_title(title, fontsize=16, pad=15)
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True)

        x_data = self.B_function(data[:, 0])
        y_data = self.R1_function(data[:, 1])

        ax.plot(x_data, y_data, color='black', linestyle="-", linewidth=0.5, marker='o', markersize=1)
        if hline is not None:
            ax.axhline(y=hline, color="red", linestyle="--", linewidth=1)
        if vline is not None:
            ax.axvline(x=vline, color="red", linestyle="--", linewidth=1)

        plt.show()

    def double_plot(self, data1=np.array([[0, 0]]), data2=np.array([0,0]), vline=None, hline=None, x_label="x - Axis", y_label="y - Axis", title="Plot Title"):
        fig, ax = plt.subplots()
        ax.set_title(title, fontsize=16, pad=15)
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True)

        x_data1 = self.T_function(data1[:, 0])
        y_data1 = self.R3_function(data1[:, 1])

        x_data2 = self.T_function(data2[:, 0])
        y_data2 = self.R3_function(data2[:, 1])

        ax.plot(x_data1, y_data1, color='black', linestyle="-", linewidth=1)
        ax.plot(x_data2, y_data2, color='blue', linestyle="-", linewidth=1)
        if hline is not None:
            ax.axhline(y=hline, color="red", linestyle="--", linewidth=1)
        if vline is not None:
            ax.axvline(x=vline, color="red", linestyle="--", linewidth=1)

        plt.show()
