from PIL import Image, UnidentifiedImageError
import wget
import os
import time


def cut(fname):
	im = Image.open(fname)
	im_crop = im.crop((8,8, 16,16))
	im_crop2 = im.crop((40, 8, 48, 16))
	im_crop2.save("layer2.png")
	mask_im = Image.open('layer2.png').resize(im_crop.size).convert('RGBA')
	im_crop.paste(im_crop2, mask_im)
	im_crop.save(f'head-{fname}')
    
	print(f"Head was saved as 'head-{fname}' in {os.getcwd()}")
	os.remove("layer2.png")
	os.remove(fname)
	
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
		fname = name
	except UnidentifiedImageError:
		print("")
		print("Failed to find offical account, trying TL...")
		os.remove(name)
		namet = f"TL-{name}"
		fname = namet
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
			
	print("Starting creating head...")
	print("")
	cut(fname)
	print("")
	app()
app()
