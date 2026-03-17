import cv2
from NumberFromImageParser import NumberFromImageParser
from screen_capture import take_screenshot
from weapons import cs2_weapons_flat
import random

parser = NumberFromImageParser()

image = take_screenshot()
money = parser.capture_current_money(image)

print(f"Detected money: ${money}")

def getRandomWeapon(money):
    affordable_weapons = [weapon for weapon in cs2_weapons_flat if weapon["price"] <= money]
    if not affordable_weapons:
        return None
    return random.choice(affordable_weapons)

random_weapon = getRandomWeapon(money)
if random_weapon:
    print(f"Randomly selected weapon: {random_weapon['name']} (Price: ${random_weapon['price']} - Side: {random_weapon['side']})")