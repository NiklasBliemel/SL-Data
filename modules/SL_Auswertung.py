from modules import Plotter
from modules import FileReader
from pathlib import Path
import os
import numpy as np

file_reader = FileReader.FileReader()
plotter = Plotter.Plotter()


'''''
In this module are the assembled evaluations of the experiments.
Whenever there is a file as argument, you can choose which of the measurements to plot, by just writing the respective
temperature of the measurement, stored in the file names.
Some of the functions will print evaluation data in the terminal, for example the parameter of the fit-function
'''''


def spule_R_B_plot(file="6.18"):
    data = file_reader.read_file("tt Spule/" + str(file), "\t")

    y_data = data[1:, 1]

    average_y = np.mean(y_data[:10], axis=0)
    next_average_y = np.mean(y_data[10:20], axis=0)
    peak_gradient = next_average_y - average_y
    peak_gradient_index = 0

    for i in range(1, len(y_data) - 20):
        average_y = np.mean(y_data[i:(i + 10)], axis=0)
        next_average_y = np.mean(y_data[(i + 10):(i + 20)], axis=0)
        gradient = next_average_y - average_y
        if gradient > peak_gradient:
            peak_gradient = gradient
            peak_gradient_index = i + 10

    plotter.plot(data[1:], vline=plotter.tt_I_to_B(data[peak_gradient_index, 0]), x_label="B[T]",
                 y_label=r"R[$\Omega$]", title="", x_function=plotter.tt_I_to_B, y_function=plotter.tt_spule_U_to_R)


def spule_B_T_plot():
    data = []
    for file in Path("tt Spule").iterdir():
        try:
            file_data = file_reader.read_file(str(file), "\t")
            y_data = file_data[1:, 1]

            average_y = np.mean(y_data[:20], axis=0)
            next_average_y = np.mean(y_data[1:20], axis=0)
            peak_gradient = next_average_y - average_y
            peak_gradient_index = 0

            for i in range(1, len(y_data) - 20):
                average_y = np.mean(y_data[i:(i + 10)], axis=0)
                next_average_y = np.mean(y_data[(i + 10):(i + 20)], axis=0)
                gradient = next_average_y - average_y
                if gradient > peak_gradient:
                    peak_gradient = gradient
                    peak_gradient_index = i + 1

            data.append([float(str(file).split("/")[-1]), file_data[peak_gradient_index, 0] - 0.1])
        except UnicodeDecodeError as e:
            print(e)

    data = np.array(data)
    data = data[np.argsort(data[:, 0])]

    plotter.plot_with_fit(data, x_label="T[K]", y_label="B[T]", title="")


def film_R_B_plot(file="8.50"):
    data = file_reader.read_file("tt-Teil film/" + str(file), "\t")

    y_data = data[1:, 1]

    average_y = np.mean(y_data[:10], axis=0)
    next_average_y = np.mean(y_data[10:20], axis=0)
    peak_gradient = next_average_y - average_y
    peak_gradient_index = 0

    for i in range(1, len(y_data) - 20):
        average_y = np.mean(y_data[i:(i + 10)], axis=0)
        next_average_y = np.mean(y_data[(i + 10):(i + 20)], axis=0)
        gradient = next_average_y - average_y
        if gradient > peak_gradient:
            peak_gradient = gradient
            peak_gradient_index = i

    plotter.plot(data[1:], vline=plotter.tt_I_to_B(data[peak_gradient_index, 0]), x_label="B[T]",
                 y_label=r"R[$\Omega$]", title="", x_function=plotter.tt_I_to_B, y_function=plotter.tt_film_U_to_R)


def film_R_T_plot():
    data = []
    for file in Path("tt-Teil film/").iterdir():
        try:
            file_data = file_reader.read_file(str(file), "\t")
            y_data = np.mean(file_data[:20, 1], axis=0)
            data.append([float(str(file).split("/")[-1]), y_data])

        except UnicodeDecodeError as e:
            print(e)

    data = np.sort(np.array(data), axis=0)
    plotter.plot(data, x_label="T[K]", y_label=r"R[$\Omega$]", vline=8.81, title="", y_function=plotter.tt_film_U_to_R, style=2)


def film_B_T_plot():
    data = []
    for file in Path("tt-Teil film").iterdir():
        try:
            file_data = file_reader.read_file(str(file), "\t")
            y_data = file_data[1:, 1]

            average_y = np.mean(y_data[:20], axis=0)
            next_average_y = np.mean(y_data[1:20], axis=0)
            peak_gradient = next_average_y - average_y
            peak_gradient_index = 0

            for i in range(1, len(y_data) - 20):
                average_y = np.mean(y_data[i:(i + 10)], axis=0)
                next_average_y = np.mean(y_data[(i + 10):(i + 20)], axis=0)
                gradient = next_average_y - average_y
                if gradient > peak_gradient:
                    peak_gradient = gradient
                    peak_gradient_index = i

            data.append([float(str(file).split("/")[-1]), file_data[peak_gradient_index, 0] - 0.1])
        except UnicodeDecodeError as e:
            print(e)

    data = np.array(data)
    data = data[np.argsort(data[:, 0])]

    plotter.plot_with_fit(fit_start=5, data=data, x_label="T[K]", y_label="B[T]", title="")


def ht_plot():
    data_ab = file_reader.read_file("ht/Hochtemperatur_ab.txt", "\t")
    data_c = file_reader.read_file("ht/Hochtemperatur_c.txt", "\t")

    y_data_ab = data_ab[:, 1]

    average_y = np.mean(y_data_ab[:10], axis=0)
    next_average_y = np.mean(y_data_ab[10:20], axis=0)
    peak_gradient = next_average_y - average_y
    peak_gradient_index = 0

    for i in range(1, len(y_data_ab) - 20):
        average_y = np.mean(y_data_ab[i:(i + 10)], axis=0)
        next_average_y = np.mean(y_data_ab[(i + 10):(i + 20)], axis=0)
        gradient = -(next_average_y - average_y)
        if gradient > peak_gradient:
            peak_gradient = gradient
            peak_gradient_index = i + 10

    print(plotter.ht_U_to_T(data_ab[peak_gradient_index, 0]))

    plotter.double_plot(data_ab, data_c, vline=plotter.ht_U_to_T(data_ab[peak_gradient_index, 0]), x_label="T[K]",
                        y_label=r"R[$\text{m}\Omega$]", title="")
