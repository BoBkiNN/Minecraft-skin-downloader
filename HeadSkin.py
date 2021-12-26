from PIL import Image
import wget
import os
import time

def app():
	nick = input("Nickname: ")
	url = f"https://tlauncher.org/upload/all/	nickname/{nick}.png"
	name = url.split("/")
	name = name[len(name)-1]
	#print(f"Skin will be saved as {name} in {os.getcwd()}")
	if os.path.exists(name):
    	    os.remove(name)
	try:
		wget.download(url,name)
	except:
		print(f"Nickname {nick} not found")
		print("")
		time.sleep(1)
		app()
 
	im = Image.open(name)
	im_crop = im.crop((8,8, 16,16))
	print(f"Head will be saved as 'head-{name}' in {os.getcwd()}")

	im_crop.save(f'head-{name}')
	os.remove(name)
	app()
app()
