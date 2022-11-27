import socket, base64
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode


def main(qrcode_base64):
    """ Decodage de qrcode en base64. """
    qrcode = Image.open(BytesIO(base64.b64decode(qrcode_base64)))
    width, height = qrcode.size

    # Liste des valeurs des pixels pour chaque quart
    quarter_list = [[],[],[],[]]

    # Quart 1
    for y in range(0, height//2):
        for x in range(0, width//2):
            quarter_list[0].append(qrcode.getpixel((x,y)))
    quarter1 = Image.new("RGB", (width//2, height//2))
    quarter1.putdata(quarter_list[0])

    # Quart 2 + inversion des couleurs
    for y in range(0, height//2):
        for x in range(width//2, width):
            if qrcode.getpixel((x,y)) == (255, 255, 255):
                quarter_list[1].append((0, 0, 0))
            else:
                quarter_list[1].append((255, 255, 255))
    quarter2 = Image.new("RGB", (width//2+1, height//2))
    quarter2.putdata(quarter_list[1])

    # Quart 3 + inversion des couleurs
    for y in range(height//2, height):
        for x in range(0, width//2):
            if qrcode.getpixel((x,y)) == (255, 255, 255):
                quarter_list[2].append((0, 0, 0))
            else:
                quarter_list[2].append((255, 255, 255))
    quarter3 = Image.new("RGB", (width//2, height//2+1))
    quarter3.putdata(quarter_list[2])

    # Quart 4
    for y in range(height//2, height):
        for x in range(width//2, width):
            quarter_list[3].append(qrcode.getpixel((x,y)))
    quarter4 = Image.new("RGB", (width//2+1, height//2+1))
    quarter4.putdata(quarter_list[3])

    # Reconstitution du QR Code original
    all_quarter = Image.new('RGB', (width, height)).convert("RGB")
    try:
        # Translation verticale
        all_quarter.paste(quarter3, (0, 0))
        all_quarter.paste(quarter4, (width//2, 0))
        all_quarter.paste(quarter1, (0, height//2))
        all_quarter.paste(quarter2, (width//2, height//2))
        result = decode(all_quarter)
        assert(len(result) > 0),"Erreur: Lecture impossible"
    except:
        # Translation horizontale
        all_quarter.paste(quarter2, (0, 0))
        all_quarter.paste(quarter1, (width//2, 0))
        all_quarter.paste(quarter4, (0, height//2))
        all_quarter.paste(quarter3, (width//2, height//2))
        result = decode(all_quarter)
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
