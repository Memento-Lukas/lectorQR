import qrcode
from PIL import Image

textoQR = input("Introducir URL para código QR: ") 
codigoImg = qrcode.make(textoQR)

nombreQR = input("Introducir nombre para el archivo generado: ") + '.png'
imagenFile = open(nombreQR, 'wb')

codigoImg.save(imagenFile)
imagenFile.close()

rutaCodigo = './' + nombreQR
Image.open(rutaCodigo).show()
