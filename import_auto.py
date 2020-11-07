import os
import shutil
import random


def import_fichier_train():

    CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]

    if not os.path.exists("dataset_reduit_train"):
        os.makedirs("dataset_reduit_train")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"dataset_reduit_train/{letter}"):
            os.makedirs(f"dataset_reduit_train/{letter}")
            for file in os.listdir(f"data/alphabet-dataset/{letter}/"):
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"dataset_reduit_train/{letter}")
                i += 1
                if i == 200:
                    break

def import_fichier_test():

    CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]

    if not os.path.exists("dataset_reduit_test"):
        os.makedirs("dataset_reduit_test")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"dataset_reduit_test/{letter}"):
            os.makedirs(f"dataset_reduit_test/{letter}")
            file_list = os.listdir(f"data/alphabet-dataset/{letter}/")
            random.shuffle(file_list)
            for file in file_list:
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"dataset_reduit_test/{letter}")
                i += 1
                if i == 3:
                    break
