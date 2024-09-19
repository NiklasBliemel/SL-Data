import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


'''''
This module is used to plot the data.
It contains functions specifically made to convert the out put data of the experiment to the
desired Unit.
'''''


class Plotter:
    def __init__(self):
        self.mu_o = 4 * np.pi * 1e-7
        self.l_ext = 15.8 * 1e-2
        self.N_ext = 6245
        self.I_const = 8e-6
        self.I_ht_const = 1.95 * 1e-3

    def model_function_B_T(self, x, B_C, T_C):
        return B_C * (1 - (x / T_C) ** 2)

    def tt_I_to_B(self, x):
        return (self.mu_o * x * self.N_ext) / self.l_ext

    def tt_film_U_to_R(self, x):
        return x * 3e-3 / self.I_const

    def tt_spule_U_to_R(self, x):
        return x * 1e-2 / self.I_const

    def ht_U_to_R(self, x):
        return (x / self.I_ht_const) * 1e3

    def ht_U_to_T(self, x):
        return np.sqrt((x * 1e6)/0.0637 + 16111) - 49.5

    def plot_with_fit(self, fit_start=0, data=np.array([[0, 0]]), x_label="x - Axis", y_label="y - Axis", title="Plot Title"):
        fig, ax = plt.subplots()
        ax.set_title(title, fontsize=16, pad=15)
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True)

        x_data = data[:, 0]
        y_data = self.tt_I_to_B(data[:, 1])

        ax.plot(x_data, y_data, color='black', linestyle="", marker='o', markersize=5)

        popt, pcov = curve_fit(self.model_function_B_T, x_data, y_data, p0=[1, 1])

        x_fit = np.linspace(fit_start, max(x_data), 1000)
        y_fit = self.model_function_B_T(x_fit, *popt)

        ax.plot(x_fit, y_fit, color='red', linestyle="-", label=r"$B_c(T)\left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]$")
        ax.legend(loc='best', draggable=True)

        print(popt, np.diag(pcov))

        plt.show()

    def plot(self, data=np.array([[0, 0]]), vline=None, hline=None, x_label="x - Axis", y_label="y - Axis", title="Plot Title", x_function=None, y_function=None):
        fig, ax = plt.subplots()
        ax.set_title(title, fontsize=16, pad=15)
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True)

        x_data = x_function(data[:, 0])
        y_data = y_function(data[:, 1])

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

        x_data1 = self.ht_U_to_T(data1[:, 0])
        y_data1 = self.ht_U_to_R(data1[:, 1])

        x_data2 = self.ht_U_to_T(data2[:, 0])
        y_data2 = self.ht_U_to_R(data2[:, 1])

        ax.plot(x_data1, y_data1, color='black', linestyle="-", linewidth=1)
        ax.plot(x_data2, y_data2, color='blue', linestyle="-", linewidth=1)
        if hline is not None:
            ax.axhline(y=hline, color="red", linestyle="--", linewidth=1)
        if vline is not None:
            ax.axvline(x=vline, color="red", linestyle="--", linewidth=1)

        plt.show()
