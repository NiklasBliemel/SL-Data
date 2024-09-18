import numpy as np


class FileReader:
    def read_file(self, file_path, sep=";"):
        data = []
        with open(file_path, "r") as file:
            for line in file:
                line = line.replace(",", ".")
                if sep in line:
                    data.append(line.strip().split(sep))
        return np.array(data).astype(float)
