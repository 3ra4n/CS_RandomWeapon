import cv2
import pytesseract
import re
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

class NumberFromImageParser:
    def capture_current_money(self, image):
        #Make sure to crop only the area where the money is displayed in the game
        print("Capturing money from image...")
        money_region = image[1020:1060, 0:140]  # Adjust these values based on your screen resolution
        cv2.imwrite("money_crop.png", money_region) # Save the cropped image for debugging


        print("Preprocessing image for OCR...")
        grey = cv2.cvtColor(money_region, cv2.COLOR_BGR2GRAY)
        #thresholding to make the text more clear for OCR
        _, thresh = cv2.threshold(grey, 150, 255, cv2.THRESH_BINARY)

        print("Converting image for OCR...")
        pil_image = Image.fromarray(thresh)
        text = pytesseract.image_to_string(pil_image, config='--psm 7 ')

        print(f"OCR raw output: '{text}'")
        match = re.search(r'\$(\d+)', text)
        return int(match.group(1)) if match else None
        
        