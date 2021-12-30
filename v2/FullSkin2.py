import wget
from PIL import Image, UnidentifiedImageError
import os
import time

def app():
	nick = input("Nickname: ")
	url = f"https://tlauncher.org/upload/all/nickname/{nick}.png"
	urlt = f"https://tlauncher.org/upload/all/nickname/tlauncher_{nick}.png"
	#print(url,urlt)
	name = url.split("/")
	name = name[len(name)-1]
	#print(name)

	if os.path.exists(name):
	    	    os.remove(name)
	
	wget.download(url, name)
	print("")
	
	try:
		ch = Image.open(name)
		print(f"Skin was saved to {os.getcwd()}/{name}")
		print("")
	except UnidentifiedImageError:
		print("")
		print("Failed to find offical account, trying TL...")
		os.remove(name)
		namet = f"TL-{name}"
		print("")
		if os.path.exists(namet):
	    	    os.remove(namet)
		wget.download(urlt,namet)
		print("")
		
		#check is file work
		try:
			ch = Image.open(namet)
			print(f"Skin was saved to {os.getcwd()}/{namet}")
			print("")
		except UnidentifiedImageError:
			print("")
			print("Account not found")
			print("")
			os.remove(namet)
			time.sleep(1)
	
	app()
app()
