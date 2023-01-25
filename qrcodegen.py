__author__ = "Steven Geerts"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "Unlicensed"
__version__ = "1.0.0"
__maintainer__ = "Steven Geerts"
__status__ = "Development"

# script is only tested with python3.9 on OSX
# use pip3.9 install qrcode

import sys
import qrcode
from credentials import credentials

background = (123, 198, 219)
fill_color = (38, 24, 66)

# a dict on the name + weblink
# name: the name to give to the filename that will be later saved
# link: a weblink to the file that will be used in the qr code
weblinks = {
    "name of the png file to give": "weblink"
}

emails = {
    "yourname": "emailaddress"
}

def check_pythonversion():
    if int(sys.version_info[0]) != 3 and int(sys.version_info[1]) != 9:
        print(sys.version_info[0])
        exit(-1)


def generate_qrcode(name, link, background=background, fill_color=fill_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )
    img = qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(back_color=background, fill_color=fill_color)

    name = name + ".png"
    img.save(name)


if __name__ == '__main__':
    check_pythonversion()

    c = credentials("name ")
    c.firstname = "firstname"
    c.lastname = "lastname"
    c.birthday = "birthday"
    c.address = "address"
    c.cellphonenumber = "cellphonenumber"
    c.homeemail = "homeemail"
    generate_qrcode(c.name,c.vcard())
