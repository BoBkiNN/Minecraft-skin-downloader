import wget
import os
import time

def app():
	nick = input("Nickname: ")
	url = f"https://tlauncher.org/upload/all/nickname/{nick}.png"
	urlt = f"https://tlauncher.org/upload/all/nickname/tlauncher_{nick}.png"
	name = url.split("/")
	name = name[len(name)-1]
	print(f"Skin will be saved as {name}")

	if os.path.exists(name):
	    	    os.remove(name)
	try:
			wget.download(url,name)
	except:
		try:
			wget.download(urlt, f"tlauncher_{name}")
		except:
			print(f"Nickname {nick} not found")
			print("")
			time.sleep(1)
			app()
	app()
app()
