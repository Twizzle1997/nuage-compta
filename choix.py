import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import keras
from keras import metrics
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation
import os
import pickle


def choix_result(choix_image):

    choix = (r"{}".format(choix_image))
    test_image = image.load_img(choix, target_size = (32,32))
    plt.imshow(test_image)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    resultat = model.predict(test_image)
    resultat = get_result(resultat)
    print(f"La lettre correspondante est: {resultat}")