import cv2
import numpy as np

class Methods:

    def get_result(result):
        if result[0][0] == 1:
            return("A")
        elif result[0][1] == 1:
            return ("B")
        elif result[0][2] == 1:
            return ("C")
        elif result[0][3] == 1:
            return ("D")
        elif result[0][4] == 1:
            return ("E")
        elif result[0][5] == 1:
            return ("F")
        elif result[0][6] == 1:
            return ("G")
        elif result[0][7] == 1:
            return ("H")
        elif result[0][8] == 1:
            return ("I")
        elif result[0][9] == 1:
            return ("J")
        elif result[0][10] == 1:
            return ("K")
        elif result[0][11] == 1:
            return ("L")
        elif result[0][12] == 1:
            return ("M")
        elif result[0][13] == 1:
            return ("N")
        elif result[0][14] == 1:
            return ("O")
        elif result[0][15] == 1:
            return ("P")
        elif result[0][16] == 1:
            return ("Q")
        elif result[0][17] == 1:
            return ("R")
        elif result[0][18] == 1:
            return ("S")
        elif result[0][19] == 1:
            return ("T")
        elif result[0][20] == 1:
            return ("U")
        elif result[0][21] == 1:
            return ("V")
        elif result[0][22] == 1:
            return ("W")
        elif result[0][23] == 1:
            return ("X")
        elif result[0][24] == 1:
            return ("Y")
        elif result[0][25] == 1:
            return ("Z")
        elif result[0][26] == 1:
            return("♡")

    def negatif(entree, sortie):
        img = cv2.imread(entree)
        cv2.imshow("Pic", img)
        img_negatif = cv2.bitwise_not(img)
        cv2.imwrite(sortie, img_negatif)

    def resize_image(img, size=(20,20)):

        h, w = img.shape[:2]
        
        if h == w: 
            return cv2.resize(img, size, cv2.INTER_AREA)

        dif = h if h > w else w


        if dif > (size[0] + size[1]):
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC

        x_pos = (dif - w)//2
        y_pos = (dif - h)//2

        mask = np.zeros((dif, dif), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]

        return cv2.resize(mask, size, interpolation)

    def getContours(img,imgContour):
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            areaMin = cv2.getTrackbarPos("Area", "Parameters")
            if area > areaMin:
                cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                print(len(approx))
                x , y , w, h = cv2.boundingRect(approx)
                cv2.rectangle(imgContour, (x , y ), (x + w , y + h ), (0, 255, 0), 5)

                cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                            (0, 255, 0), 2)
                cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (0, 255, 0), 2)