import cv2
from NumberFromImageParser import NumberFromImageParser
from screen_capture import take_screenshot
from weapons import cs2_weapons, cs2_weapons_flat
import random

parser = NumberFromImageParser()

image = take_screenshot()
money = parser.capture_current_money(image)

print(f"Detected money: ${money}")

def getRandomWeapon(money):
    #Pick Random Pistol
    affordable_pistols = [w for w in cs2_weapons["pistols"] if w["price"] <= money]
    random_pistol = random.choice(affordable_pistols) if affordable_pistols else None

    other_weapons = cs2_weapons["mid_tier"] + cs2_weapons["rifles"]
    other_weapons = [w for w in other_weapons if w["price"] <= money]
    random_other = random.choice(other_weapons) if other_weapons else None
    
    return random_pistol, random_other

if money is None:
    print("Could not detect money. Please Try again.")
else:
    pistol, other = getRandomWeapon(money)
    if pistol:
        print(f"Randomly selected pistol: {pistol['name']} (Price: ${pistol['price']} - Side: {pistol['side']})")
    if other:
        print(f"Randomly selected weapon: {other['name']} (Price: ${other['price']} - Side: {other['side']})")