import cv2
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import*
from skimage import io



class FaceRecMain:

    facesNum = 0

    def openCleanImage(User_Image):
        tfd = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        img = io.imread(User_Image)

        img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

        coordinates_f = tfd.detectMultiScale(img_gray,scaleFactor= 1.05 , minNeighbors= 5)



        for (x,y,w,h) in coordinates_f:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,00),10)
            FaceRecMain.facesNum+=1


        img_returned = Image.fromarray(img)

        pixmap = QPixmap.fromImage(ImageQt(img_returned))




        return pixmap











