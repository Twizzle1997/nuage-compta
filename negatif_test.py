

from PIL import Image, ImageOps


im = Image.open('data/src/horse.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('data/dst/horse_invert.png')