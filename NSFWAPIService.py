import json

import requests
import cv2
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import*
from skimage import io



class NSFWAPIService:

    def getNSFW(self,pUrl):


        if pUrl == None:
           self.getNSFW(self,pUrl)
        else:
            url = "https://nsfw-image-classification1.p.rapidapi.com/img/nsfw"

            payload = {
                "url": pUrl
            }

            headers = {
                'content-type': "application/json",
                'x-rapidapi-key': "fe972c93b2msh15a7a2f0c33366bp16c8cdjsncbbe2f4acceb",
                'x-rapidapi-host': "nsfw-image-classification1.p.rapidapi.com"
            }

            response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
            numberNSFW = response.json()

            print(numberNSFW['NSFW_Prob'])

            return numberNSFW['NSFW_Prob'] * 100

    def getNSFWImage(userI):

        img = io.imread(userI)

        blurred_Image = cv2.blur(img,(300,300),cv2.BORDER_DEFAULT)

        img_returned = Image.fromarray(blurred_Image)

        pixmap = QPixmap.fromImage(ImageQt(img_returned))

        return  pixmap





