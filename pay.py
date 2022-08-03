from promptpay import qrcode
from PIL import Image
import os

import sys
print(sys.path)
print("Current working directory: {0}".format(os.getcwd()))

print("Current working directory: {0}".format(os.getcwd()))

# generate a payload
id_or_phone_number = "0892343728"
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 500.01)

# export to PIL image
img = qrcode.to_image(payload)
img23 = qrcode.to_image(payload_with_amount )
#print(payload)#
xx = qrcode.to_file(payload_with_amount, "./qrcode/0892343728.png")
#qrcode.to_file(payload_with_amount, "/Users/User/Downloads/qrcode-0892343728.png") 
print(type(img23))
print(img23.size)
img23.save('./qrcode/qrcode_test.png')
images = Image.open('./qrcode/qrcode_test.png')
images.show()
