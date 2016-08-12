from PIL import Image
    im = Image.open("puppy.jpg")
    im.rotate(45).show()
new_image.save("output.jpg", "jpeg")

# skeleton code for obamicon 
from PIL import Image
# =============================================================== 
# define colors as variables so we can recall them later: 
# dark blue: (0, 51, 76) 
# red: (217, 26, 33) 
# light blue: (112, 150, 158) 
# yellow: (252, 227, 166) 
# =============================================================== 
dark_blue = (0, 51, 76) 
red = (217, 26, 33) 
light_blue = (112, 150, 158) 
yellow = (252, 227, 166)
# =============================================================== 
# define a function that obama-fies the image. 
# this function will take your images' pixel list as a parameter. 
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture. 
# =============================================================== 
def obamafy(pixel_list):
	obamafied_pixel_list = list(im.getdata()) 
	# BEHAVIOR UNDEFINED 
	for pixel in im.getdata():
		red = pixel [0]
		green = pixel [1]
		blue = pixel [2]
		total = red + green + blue 
		if total > 182 
			append.obamafied_pixel_list(dark blue)
		if 364> total > 182
			apppend.obamafied_pixel_list(red)
		if 546> total > 364
			append.obamafied_pixel_list(light blue)
		if total > 546
			append.obamafied_pixel_list(yellow)
	return obamafied_pixel_list
	
# =============================================================== 
# ask the user for the image name and open the image 
# =============================================================== 
my_image = turtlee.jpg # UNDEFINED

# =============================================================== 
# convert the image into a list of pixel RGB values 
# =============================================================== my_image_pixel_list = None # UNDEFINED

# =============================================================== 
# obamafy your image by calling your function 
# =============================================================== obamafied_pixels = obamafy(my_image_pixel_list)

# =============================================================== 
# create a new image and copy the new obama-fied pixel list into the image 
# =============================================================== obamafied_image = None # UNDEFINED

# =============================================================== 
# finally, show and save the image 
# ===============================================================