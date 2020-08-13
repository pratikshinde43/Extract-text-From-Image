import json

import pytesseract
import cv2
import numpy
from PIL import Image
import datetime
import re



class TextExtraction:
		
	
	def NormalImage(self,image):
		text = pytesseract.image_to_string(image, lang = 'eng')
		#print(text)
		words = text.split('\n')
		print(words)

		if len(words) > 0:
			self.BlackWhite(image)
		else:
			pass

		
			
	def resize(self,image):
			width, height = image.size
			new_size = width * 6, height * 6
				
				# scaling the image through LANCZOS
				
			img = image.resize(new_size, Image.LANCZOS)
				
			text = pytesseract.image_to_string(img, lang='eng')
			#print(text)
			words = text.split('\n')
			print(words)
			if len(words) > 0:
				print(words)
			else:
				print("Data Not Found")
			
			

	def BlackWhite(self,image):
#changing the size of small size image

		
		#img.save('resize.jpg')

# converting the pillow type image to opencv

		open_cv_image = numpy.array(image)
		open_cv_image = open_cv_image[:, :, ::-1].copy()

#converting the image to grayscale and changing the black and white pizel value

		gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
		(thresh, blackAndWhiteImage) = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY)
		cv2.imwrite('blackandwhite.jpg', blackAndWhiteImage)

# giving the image to TESSERACT for OCR

		text = pytesseract.image_to_string(img, lang = 'eng')
		#print(text)
		words = text.split('\n')
		print(words)
		if len(words) > 0:
			self.resize(image)
		else:
			pass



# taking the input of the image


