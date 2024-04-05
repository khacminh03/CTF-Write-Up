from PIL import Image, ImageChops
image1 = Image.open("flag.png")
image2 = Image.open("lemur.png")
diff = ImageChops.difference(image1, image2)
diff.show()