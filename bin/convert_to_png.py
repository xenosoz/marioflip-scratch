#!/usr/bin/env python
from PIL import Image
from os.path import splitext

def convert(pathname):
    filename, ext = splitext(pathname)
    im = Image.open(pathname)
    
    new_pathname = "%s%s" % (filename, ".png")
    im.save(new_pathname)
    print new_pathname

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        convert(sys.argv[1])
