import os
import base64

PATH = os.path.dirname(os.path.abspath(__file__))

def save_file(passport_pic):
    if passport_pic:
        target = os.path.join(PATH, 'passport_pics/')
        
        if not os.path.isdir(target):
            os.mkdir("/".join([target, passport_pic]))
        imgdata = base64.b64decode(passport_pic)
        destination = "/".join([target, passport_pic])
        with open(destination, 'wb') as f:
            f.write(imgdata)