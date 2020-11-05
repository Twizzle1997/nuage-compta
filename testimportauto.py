import os
import shutil


import os

if not os.path.exists("data_set_reduit"):
    os.mkdir("data_set_reduit")
    os.mkdir("data_set_reduit/a")
    os.mkdir("data_set_reduit/b")
    os.mkdir("data_set_reduit/c")
    os.mkdir("data_set_reduit/d")
    os.mkdir("data_set_reduit/e")
    os.mkdir("data_set_reduit/f")
    os.mkdir("data_set_reduit/g")
    os.mkdir("data_set_reduit/h")
    os.mkdir("data_set_reduit/i")
    os.mkdir("data_set_reduit/j")
    os.mkdir("data_set_reduit/k")
    os.mkdir("data_set_reduit/l")
    os.mkdir("data_set_reduit/m")
    os.mkdir("data_set_reduit/n")
    os.mkdir("data_set_reduit/o")
    os.mkdir("data_set_reduit/p")
    os.mkdir("data_set_reduit/r")
    os.mkdir("data_set_reduit/s")
    os.mkdir("data_set_reduit/t")
    os.mkdir("data_set_reduit/u")
    os.mkdir("data_set_reduit/v")
    os.mkdir("data_set_reduit/w")
    os.mkdir("data_set_reduit/x")
    os.mkdir("data_set_reduit/y")
    os.mkdir("data_set_reduit/z")
    os.mkdir("data_set_reduit/z_coeur")

    filePath = shutil.copy("data/alphabet-dataset/A/"[:2], "data_set_reduit/a")
    print(filePath)    #cela affiche /home/user/doc/file.txt

else:
    print("Dossier déjà éxistant! ")

