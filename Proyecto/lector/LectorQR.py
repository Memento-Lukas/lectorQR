import cv2
import ezodf
import sys

_, rutaArchivo, hojaCalc, fila = sys.argv

fila = int(fila)
ods = ezodf.newdoc(doctype='ods', filename=rutaArchivo)
sheet = ezodf.Sheet(hojaCalc, size=(10, 10))
ods.sheets+=sheet

capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()

    if cv2.waitKey(1) == ord('s'):
        break

    detectorQR = cv2.QRCodeDetector()
    try:
        data, bbox, imagenRectificada = detectorQR.detectAndDecode(frame)
    except:
        print(f"Error en la detección de código QR")
        data = ""
        bbox = []
        imagenRectificada = frame

    if len(data) > 0:
        save = None
        while save not in ['y', 'n']:
            save = input(f'Dato: {data}' + '\nDesea guardar? [y/n]:')
            if save == 'y':
                # Establecer el valor en la celda
                sheet[f'A{fila}'].set_value(data)
                fila+=1
            else:
                break

        print(f'Dato: {data}')
        cv2.imshow('webCam', imagenRectificada)
    else:
        cv2.imshow('webCam', frame)

ods.save()
capture.release()
cv2.destroyAllWindows()
