print("toto")



import os
import shutil



CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "Y", "V", "W", "X", "Y", "Z"]

if not os.path.exists("data_set_reduit"):
    os.makedirs("data_set_reduit")
for letter in CATEGORIES:
    i = 0
    if not os.path.exists(f"data_set_reduit/{letter}"):
        os.makedirs(f"data_set_reduit/{letter}")
        for file in os.listdir(f"data/alphabet-dataset/{letter}/"):
            shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"data_set_reduit/{letter}")
            i += 1
            if i == 200:
                break

