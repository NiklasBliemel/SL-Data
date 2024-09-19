import numpy as np


'''''
File Reader can read any txt file and converts the data into a numpy array, whereby
each line will be one data point and you can choose the sing which x and y data
is separated in the txt file.
'''''


class FileReader:
    def read_file(self, file_path, sep=";"):
        data = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.replace(",", ".")
                if sep in line:
                    data.append(line.strip().split(sep))
        return np.array(data).astype(float)
