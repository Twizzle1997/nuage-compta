# nuage-compta
Brief Nuage Compta

### Audrey Cornaire / Nicolas Campion / Thomas Cassagne

![Screenshot](https://github.com/Twizzle1997/nuage-compta/blob/tom/assets/Capture.PNG?raw=true)

## Librairies principales
*Un fichier environment à été généré afin d'installer le bon environnement ainsi que TOUTES les librairies necessaires*

* import numpy as np
* import matplotlib
* from keras
* import os
* import pickle
* import cv2
* import imutils




## Sources

* https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Intermediate/RealTime_Shape_Detection_Contours.py
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

## 1. La création du modèle

La création de notre modèle se trouve dans le fichier creation_modele.ipynb

Nous avons décidé d'importer 200 images pour la phase de d'entrainement et 60 images pour la phase de test d'entrainement de notre modèle grâce aux fonctions : 
* import_fichier_train
* import_fichier_test

Ensuite, nous avons "dessiné" notre modèle en commencant par lui soumettre les donées de base :

* target size
* batch size
* class mode
* color mode

```PYTHON

train_generator = train_datagen.flow_from_directory(
    ### Choix de mon repertoire ###
    directory = "data/dataset_reduit_train",
    ### Je converti les images de leur taille d'origine à notre target_size ###                    
    target_size = (28,28),
    ### Nombre batch_size qui fait référence au nombre d'exemples d'entraînement utilisés dans une itération ###                                      
    batch_size = 32,
    ### Je definis le class_mode sur "catégorical" indiquant que nous avons plusieurs classes (a à z) à prédire ###          
    class_mode = "categorical",
    ### Je choisis le color_mode "grayscale", indiquant que nous trvaillons sur une image en noir et blanc
    color_mode = "grayscale"  
    
```
Notre modèle trouve :
Found 5207 images belonging to 27 classes.
Found 1567 images belonging to 27 classes.
27 classes car nous avons ajoutés des images de coeur (fait par nos soins via photoshop) afin d'ajouter ce caractère à notre futur analyse.

En partant d'un modèle sequentiel nous avons definis et attribué des séries de filtres que nous avons répétés deux fois afin d'être le plus performant possible.

```PYTHON
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (28,28,1), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

### Ces couches sont ensuite répétées à nouveau pour améliorer les performances du modèle ###

model.add(Conv2D(32, (3, 3), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

### Enfin, nous aplatissons notre matrice résultante et la passons à travers une couche dense composée de 128 nœuds. Celui-ci est ensuite connecté à la couche de sortie constituée de 26 nœuds, chaque nœud représentant un alphabet ###

model.add(Flatten())
model.add(Dense(units = 128, activation = "relu"))
model.add(Dense(units = 27, activation = "softmax"))            ### Activation softmax qui convertit les scores en une distribution de probabilité normalisée, et                                                                   le nœud avec la probabilité la plus élevée est sélectionné comme sortie ###

### Une fois notre architecture CNN définie, nous compilons le modèle à l'aide de l'optimiseur Adam ###
model.compile(optimizer = "adam", loss = "categorical_crossentropy", metrics = ["accuracy"])

model.summary()
```


## 2. L'entrainement et enregistrement du modèle

En definissant un nombre d'epoch et d'étape par epoch assez élevées (ici *2 par rapport à la source) nous arrivons à un modèle qui possède une "fiabilité" de presque 91 %

```PYTHON
entrainement = model.fit_generator(
    train_generator,
    steps_per_epoch = 32,
    epochs = 35,
    validation_data = test_generator,
    validation_steps = 32
)

score = model.evaluate(train_generator, verbose=0)
print("Test de perte:", score[0])
print("Test de précision:", score[1])
print("Enregistrement du modèle...")
model.save("data/model.h5")
print("Modèle enregistré!")
```

Test de perte: 0.5439829230308533
Test de précision: 0.9099289178848267
Enregistrement du modèle...
Modèle enregistré!


## 2. Le test du modèle

Après avoir chargé notre image reference (dans le dossier "assets") ainsi que notre modèle ici : model.h5

![Screenshot](https://github.com/Twizzle1997/nuage-compta/blob/develop/assets/imagedentrainement.jpeg?raw=true)

Nous appliquons une série de filtre sur notre image "FORMATION DATA IA ♡"

```PYTHON
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray,5)
### Détection des contours ###
blurred = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
edged = cv2.Canny(blurred, 170, 255)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sort_contours(cnts, method="left-to-right")[0]
```

Viennent ensuite la détection des ROI (region of interest) encapsulé dans une boucle for afin de parcourir chaqu'une de nos lettres présentes dans notre image de référence

```PYTHON
### Détection des ROI ###

for c in cnts:
    
    (x, y, w, h) = cv2.boundingRect(c)
    
    if (w >= 5) and (h >= 15):
        
        roi = gray[y:y + h, x:x + w]
        thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        (tH, tW) = thresh.shape
        
        if tW > tH:
            thresh = imutils.resize(thresh, width=28)
        else:
            thresh = imutils.resize(thresh, height=28)

        padded = cv2.copyMakeBorder(thresh, top=4, bottom=4,
                                    left=4, right=4, borderType=cv2.BORDER_CONSTANT,
                                    value=(0, 0, 0))
        
        padded = cv2.resize(padded, (28, 28))
        padded = padded.astype("float32") / 255.0
        padded = np.expand_dims(padded, axis=-1)
        ### Mise à jour notre liste de caractères qui seront OCR ###
        chars.append((padded, (x, y, w, h)))

```

```PYTHON
plt.imshow(image)
```

![Screenshot](https://github.com/Twizzle1997/nuage-compta/blob/develop/assets/Captulre.PNG?raw=true)






