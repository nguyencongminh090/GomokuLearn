import pyautogui
from PIL import Image
import cv2
import json


def resize_image(image):
    image = cv2.imread(image)
    dim = (350, 350)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    image = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(image)
    return im_pil
    

f = open('setting.json', 'r')
k = json.load(f)
img_name = k['img_name']
img = pyautogui.screenshot(region=(5, 114, 550, 550))
img.save(img_name)
img = resize_image(img_name)
img.save(img_name)
