import cv2



def negatif(img_entree, img_sortie):
    img = cv2.imread(img_entree)                               # charge une image sous forme d'array numpy de type uint8 (valeurs entre 0 et 255) de dimensions (hauteur, largeur, 3) pour une image couleur (si pas d'image, renvoie None).
    cv2.imshow("Pic",img)                                                               # cv2.imshow('myImage', img); cv2.waitKey(2000); cv2.destroyImage('myImage') : affiche l'image pendant 2000 ms et si on tape une touche pendant cetter période, la referme ensuite (attention, waitKey est indispensable pour afficher l'image). PROBLEME SUR destroyAllWindows !!!
    img_negatif = cv2.bitwise_not(img)
    cv2.imwrite(img_sortie, img_negatif)               # sauvegarde l'image dans le fichier donné, et avec le format indiqué par l'extension.




### TEST 

# negatif("../assets/imagedentrainement.jpeg", "../assets/imagedentrainement_sortie.jpeg")