import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=30, border=4,)
qr.add_data("https://nikson1122.github.io/nstha/contact.html")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("Nikson_web.png")
















