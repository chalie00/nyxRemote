import cv2
import pytesseract
import pyocr
import numpy as np

from PIL import Image, ImageGrab


# HSV 색상(Hue), 채도(Saturation), 명도(Value)의 좌표
def image_to_string_with_hsk(image_path):
    # Specify a Tesseract directory
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load The Image
    read_img = cv2.imread(fr'{image_path}')

    # Up-Sample
    read_img = cv2.resize(read_img, (0, 0), fx=2, fy=2)

    # Convert to HSV
    hsv = cv2.cvtColor(read_img, cv2.COLOR_BGR2HSV)

    # Get Binary Mask
    msk = cv2.inRange(hsv, np.array([0, 0, 123]), np.array([179, 255, 255]))
    txt_return = pytesseract.image_to_string(msk)

    return txt_return


def image_to_string_with_lim(image_path):
    # Specify a Tesseract directory
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load The Image
    read_img = cv2.imread(fr'{image_path}')

    # Convert To Gray
    gray = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)

    # Use Limit Value
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    txt_return = pytesseract.image_to_string(gray)

    return txt_return


def image_to_string_with_blur(image_path):
    # Specify a Tesseract directory
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load The Image
    read_img = cv2.imread(fr'{image_path}')

    # Convert To Gray
    gray = cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY)

    # Use Blur
    blur = cv2.medianBlur(gray, 9)

    txt_return = pytesseract.image_to_string(blur)

    return txt_return


# Create txt with pyocr
def image_to_string_with_pyocr(img_path):
    pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    tools = pyocr.get_available_tools()
    tool = tools[0]
    txt = tool.image_to_string(Image.open(img_path), lang='eng')

    return txt


def generate_txt_array_with_img(processed_img, txt_title):
    note_memo = open(fr'Text\{txt_title}.txt', 'w+')
    for i in processed_img:
        note_memo.write(i)
    note_memo.close()

    note_memo = open(fr'Text\{txt_title}.txt', 'r+')
    note_memo = note_memo.readlines()
    note_memo = [line.strip() for line in note_memo]
    note_memo = [v for v in note_memo if v]

    return note_memo
