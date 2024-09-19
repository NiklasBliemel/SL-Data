from modules import Plotter
from modules import FileReader
from pathlib import Path
import os
import numpy as np

file_reader = FileReader.FileReader()
plotter = Plotter.Plotter()


def spule_R_B_plot(file):
    data = file_reader.read_file("tt Spule/" + file, "\t")

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

    plotter.plot(data[1:], vline=plotter.B_function(data[peak_gradient_index, 0]), x_label="B[T]",
                 y_label=r"R[$\Omega$]", title="")


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


def film_R_B_plot(file):
    data = file_reader.read_file("tt-Teil film/" + file, "\t")

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

    plotter.plot(data[1:], vline=plotter.B_function(data[peak_gradient_index, 0]), x_label="B[T]",
                 y_label=r"R[$\Omega$]", title="")


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

    plotter.plot_with_fit(data, x_label="T[K]", y_label="B[T]", title="")


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

    print(plotter.T_function(data_ab[peak_gradient_index, 0]))

    plotter.double_plot(data_ab, data_c, vline=plotter.T_function(data_ab[peak_gradient_index, 0]), x_label="T[K]",
                 y_label=r"R[$\text{m}\Omega$]", title="")
