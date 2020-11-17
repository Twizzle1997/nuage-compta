# nuage-compta
Brief Nuage Compta

### Audrey Cornaire / Nicolas Campion / Thomas Cassagne

![Screenshot](https://github.com/Twizzle1997/nuage-compta/blob/tom/assets/Capture.PNG?raw=true)

## Librairies

* import numpy as np
* import matplotlib.pyplot as plt
* from keras.preprocessing.image import ImageDataGenerator
* from keras.preprocessing import image
* import keras
* from keras import metrics
* from keras.models import Sequential
* from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation
* import os
* import pickle
* import cv2

## Sources

* https://towardsdatascience.com/building-and-deploying-an-alphabet-recognition-system-7ab59654c676
* https://note.nkmk.me/en/python-pillow-invert/
* http://courty.fr/deep-learning-03-reconnaissance-de-caracteres/
* https://lesdieuxducode.com/blog/2019/1/prototyper-un-reseau-de-neurones-avec-keras
* http://www.python-simple.com/python-opencv/lecture-sauvegarde-image.php
* https://stackoverrun.com/fr/q/12647967 

## Contexte du projet

La société Nuage est une société éditrice d'un logiciel spécialisé dans la gestion de la comptabilité pour les entreprises de toutes tailles : Nuage Compta.

Suite a un sondage auprès de ses clients sur les principales améliorations qu'ils souhaitaient voir intégrer dans le logiciel, la société souhaite développer un modèle de reconnaisance de texte appliqué aux factures de ses clients. Le but de ce modèle serait les aider dans la saisie comptable des pièces de type facture.

La société ne possède pas les ressources nécessaires pour développer un tel module et vous sollicite afin de l'aider à créer ce système.

## Les contraintes

Vous utiliserez les frameworks de Deep Learning Keras et/ou Tensorflow pour entrainer votre modèle.

Pour entrainer votre modèle, vous pouvez vous aider du jeu de données fourni et entrainer votre modèle a reconnaitre les lettres de l'alphabet.

Attention, le deep learning peut vite venir à bout des machines. Bien procéder par étape afin de comprendre le fonctionnement et la construction d'un modèle grâce au deep learning.
