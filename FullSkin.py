import wget
import os
import time

def app():
	nick = input("Nickname: ")
	url = f"https://tlauncher.org/upload/all/nickname/{nick}.png"
	urlt = f"https://tlauncher.org/upload/all/nickname/tlauncher_{nick}.png"
	name = url.split("/")
	name = name[len(name)-1]

	if os.path.exists(name):
	    	    os.remove(name)
	try:
			wget.download(url,name)
			fname = name
	except:
		try:
			wget.download(urlt, f"tlauncher_{name}")
			fname = f"tlauncher_{name}"
		except:
			print(f"Nickname {nick} not found")
			print("")
			time.sleep(1)
			app()
	print(f"Skin was saved as {fname}")
	app()
app()
