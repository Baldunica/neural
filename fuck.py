import glob,os;
from PIL import Image

size = 200, 200
'''
for infile in glob.glob('test/*/*',recursive=True):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".jpg", "JPEG")
files1 = glob.glob('test/*/*.tif',recursive=True)
for f in files1:
    os.remove(f)
'''
for infile in glob.glob('train/*/*',recursive=True):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".jpg", "JPEG")
files1 = glob.glob('train/*/*.tif',recursive=True)
for f in files1:
    os.remove(f)
print('reformatting completed')