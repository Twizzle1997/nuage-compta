import os
import shutil
import random
import cv2

def import_fichier_train():

    CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]

    if not os.path.exists("data/dataset_reduit_train"):
        os.makedirs("data/dataset_reduit_train")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"data/dataset_reduit_train/{letter}"):
            os.makedirs(f"data/dataset_reduit_train/{letter}")
            file_list = os.listdir(f"data/alphabet-dataset/{letter}/")
            random.shuffle(file_list)
            for file in file_list:
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"data/dataset_reduit_train/{letter}")
                i += 1
                if i == 200:
                    break

def import_fichier_test():

    CATEGORIES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Z_coeur_train"]

    if not os.path.exists("data/dataset_reduit_test"):
        os.makedirs("data/dataset_reduit_test")
    for letter in CATEGORIES:
        i = 0
        if not os.path.exists(f"data/dataset_reduit_test/{letter}"):
            os.makedirs(f"data/dataset_reduit_test/{letter}")
            file_list = os.listdir(f"data/alphabet-dataset/{letter}/")
            random.shuffle(file_list)
            for file in file_list:
                shutil.copy(f"data/alphabet-dataset/{letter}/{file}", f"data/dataset_reduit_test/{letter}")
                i += 1
                if i == 60:
                    break




def negatif(img_entree, img_sortie):
    img = cv2.imread(img_entree)                               # charge une image sous forme d'array numpy de type uint8 (valeurs entre 0 et 255) de dimensions (hauteur, largeur, 3) pour une image couleur (si pas d'image, renvoie None).
    cv2.imshow("Pic",img)                                                               # cv2.imshow('myImage', img); cv2.waitKey(2000); cv2.destroyImage('myImage') : affiche l'image pendant 2000 ms et si on tape une touche pendant cetter période, la referme ensuite (attention, waitKey est indispensable pour afficher l'image). PROBLEME SUR destroyAllWindows !!!
    img_negatif = cv2.bitwise_not(img)
    cv2.imwrite(img_sortie, img_negatif)               # sauvegarde l'image dans le fichier donné, et avec le format indiqué par l'extension.



def get_result(result):
    if result[0][0] == 1:
        return("a")
    elif result[0][1] == 1:
        return ("b")
    elif result[0][2] == 1:
        return ("c")
    elif result[0][3] == 1:
        return ("d")
    elif result[0][4] == 1:
        return ("e")
    elif result[0][5] == 1:
        return ("f")
    elif result[0][6] == 1:
        return ("g")
    elif result[0][7] == 1:
        return ("h")
    elif result[0][8] == 1:
        return ("i")
    elif result[0][9] == 1:
        return ("j")
    elif result[0][10] == 1:
        return ("k")
    elif result[0][11] == 1:
        return ("l")
    elif result[0][12] == 1:
        return ("m")
    elif result[0][13] == 1:
        return ("n")
    elif result[0][14] == 1:
        return ("o")
    elif result[0][15] == 1:
        return ("p")
    elif result[0][16] == 1:
        return ("q")
    elif result[0][17] == 1:
        return ("r")
    elif result[0][18] == 1:
        return ("s")
    elif result[0][19] == 1:
        return ("t")
    elif result[0][20] == 1:
        return ("u")
    elif result[0][21] == 1:
        return ("v")
    elif result[0][22] == 1:
        return ("w")
    elif result[0][23] == 1:
        return ("x")
    elif result[0][24] == 1:
        return ("y")
    elif result[0][25] == 1:
        return ("z")
    elif result[0][26] == 1:                # Création du symbole <3
        return ("♡")

