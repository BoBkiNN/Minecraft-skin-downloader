import wget
import os
import time
from PIL import Image
import functions


def choose():
    count = 0
    items = {
        1: "Get a player skin.",
        2: "Get the player's head."
    }
    print("==========---------------==========")
    print("Select an action from the list below.")
    for i in range(len(items)):
        count += 1
        print(f"{count} - {items[count]}")
    print("==========---------------==========")

    try:
        item = int(input())
        if item == 1:
            functions.skin()
        elif item == 2:
            functions.head()
    except:
        print("Try changing the value.")


while True:
    choose()
