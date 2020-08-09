from PIL import Image, ImageFilter

img = Image.open('./Pokedex/parrots.jpg')
# new_img= img.resize((400,400))
img.thumbnail((400, 400))
# new_img.save('thumbnail.jpg')
img.save('thumbnail.jpg')
print(img.size)