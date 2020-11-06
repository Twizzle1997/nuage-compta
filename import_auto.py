import os
import shutil


import os

CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "Y", "V", "W", "X", "Y", "Z","z_coeur"]

if not os.path.exists("data_set_reduit"):
    os.mkdir("data_set_reduit")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"data_set_reduit/{letter}"):
            os.mkdir(f"data_set_reduit/{letter}")
            for file in os.listdir(f"data/alphabet-dataset/{letter}/"):
                shutil.copy(file, f"data_set_reduit/{letter}")
                i += 1
                if i == 200:
                    break

