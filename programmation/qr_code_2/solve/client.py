import socket, base64
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode


def main(qrcode_base64):
    """ Decodage de qrcode en base64. """
    qrcode = Image.open(BytesIO(base64.b64decode(qrcode_base64)))
    width, height = qrcode.size

    # Rotation de l'image de 180 degrés
    qrcode = qrcode.rotate(180)

    # Inversion des couleurs pour le quart 1
    for y in range(0, height//2):
        for x in range(0, width//2):
            if qrcode.getpixel((x,y)) == (255, 255, 255):
                qrcode.putpixel((x,y), (0, 0, 0))
            else:
                qrcode.putpixel((x,y), (255, 255, 255))

    # Inversion des couleurs pour le quart 3
    for y in range(height//2, height):
        for x in range(0, width//2):
            if qrcode.getpixel((x,y)) == (255, 255, 255):
                qrcode.putpixel((x,y), (0, 0, 0))
            else:
                qrcode.putpixel((x,y), (255, 255, 255))

    result = decode(qrcode)
    assert(len(result) > 0),"Erreur: Lecture impossible"
    return result[0].data


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', 15555))

    print(server.recv(1024).decode('utf8'))
    response = input(">> ")
    server.send(response.encode('utf8'))
    
    for i in range(5):
        qrcode_base64 = server.recv(4096).decode('utf8')
        response = main(qrcode_base64)
        print(">>", response)
        server.send(response)

    print(server.recv(2048).decode('utf8'))
    server.close()
