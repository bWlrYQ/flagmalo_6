import asyncio, socket, random, base64, time

DATA_LIST = ['UHyDxXv7fHbgLdzJohFF2LYn15VFz5g60a9Yb3SwZUOqYhtPkIADb3MaxAqhkG609vSWn7uHD2RoFCgfybM98ZDyiglIRNHOnFwc',
             'KqPJKAiUqjXxcJ0QT55VwWPLV7C1l3HvvGroKrOunxWjPVUrIpsg3dYnqgCmnWEBkipXc5lfeNz4iEeFXNybYAy21ZXgPVKfCG8Q',
             '5f38Ye4xGne010J8a9CiI9SSvUGGCHtUi5cHC5b8nGFVDaPWx6iKmvnAdtF0zDlPbZZwCmjeDBlPOsJ0UIQfTecIRVUCP5s4a9QZ',
             'Ch54pBmM6nIZHd5n3UTMMC1cR12rhZki436judyDb8ytIiizkrSDfKvxabLzG2c6ZiiXgDlLuhAw9Kuc9CqXUQ7p2huU8tczZKkn',
             'TRyYRSc4MGvAXAdj8L1NFblobC5FLmMg6clPZkpAxhH45rQK01C18z0aOEOx89ccBQXE7xuOiravLBrx98UdfZN11DSYG9ll3hQC',
             'ReBoQrEtQlOerdLrwceGdQRZNS4HQ9oQfEM1zbOUCd0nZp4s3KbayJMEidbVlkeQgHYqIoSBJeX01cdrVSeCUDmvW9ubIi1gAQxC',
             '8yrAFfBqACPmPRK1r3KLwLbBOBeoMYXLjRai3tljAjtlgiKIe4NGalBRKUZPGFakvab7IpROeLhYdNQsiuLErAJRhz5z8ipWi4Dz',
             'oNba3iO0p1LJYSAX7RGPJUbuip9PbV5Mv9vPFJVxz2AhPvLLV8wAxumOpp2sPVmPKqBUrh3xdaLZxFdcwPVqY5KBbh5dIcm35TCX',
             'jgHlGLSE8xF1wPM0A3rHXNaemYryfZC8r6waP7kakMFTTQ8lfdw2Lo3vzcoO2ixUfr9BJGK34u3x6TrVraF4cuaYOqnR6kbANGgr',
             'iRQbPLqQAVRBXhBdmue1RBKRk4og0hHjmexwZBRF3pIOx8hgjfbobSidxXZuRAAOReC6Jko1XPjMByja72juk2Nt4XHHCObsyqV3',
             'DTFUDWWJIcDLPGTv31sWjFG7kFH82KVSfbKH9tyWIzD3fWJhp6NjhyTxxEQV6KKfJmgCKR0893lviE5ZjpsNR8Bf3MAq2AnzxWub',
             'SGOv3RbqdII6npaHHWxzCKuSiNKZXZaZRvyuIvDHhE5yC3rT6tUU95pOGHRoNtTNZWDIJzUmK17g89P2ZQzEzzSr7yUDCaGMo3pp',
             'f4JfaewN8A3x5p2oP4Fo6kfAQA0KbRnjIef5gT91bzLmvY21DNc1z0hgNOsGHhv8M81rnFZc0dMWug64rbzxiwo9H7TORK0MIfSA',
             'notob9MB9VYmKBPeCtG35hA84JIQNqUYMCMqDw5IRgAiVczx71WONlDd2QSWh3olfYj6LSLEsyNWZnBhpSepbjO02XTTdcB1xFZz',
             'yOv7poxKfhP6t8KTOMNfIXjUcw7n9oNIyaOAa8CfyBULMpNvdCa6MmY3Q2s4VOpMO1PRUnVjIOmDS3mpjJ4Wyrobet3IcQK4gOZB',
             'rmue8EQFkoWIreXrZPAbIo7A1L3obbKk9QyIDBuLeXf6n53BfqOHgiRE4mvjv2VXtpinZvcg3NntrkaWijplTquTuNvtV63LqWB7',
             'o4RSeIS2Po5gTi2GZG7rTQFYyArnjL1nUenI0ylgsUVooW9JnhH8bHEVQZ5TrVybXHn1Yvdk6JA1UHo1b8VwftOjbVQx6dnGPkkY',
             'lFRmH9AWLeI0Sl1aGXaNEyNoBPhMRQpJ0Uv0fq10OfAUj0LCNJsH2XThP9mQLDnz2PlhDo7lo8MSAs0U7qupEJv9THB5wEotVhBA',
             'QAWSsYgqkzXF4FiDY9qepz6rwalNo6A5ugjJ0OzSYS7CIySiakywmca1itC7t29WHHGM43R1oLkm5g0xTbvefrkELKVtYyH7PjGk',
             'CZVktwmpwzYmSgOAiajLJJbjK6Gn1rKyZqmDRcQK0s05kQMlHqfrONtBKMbRjeQzY2kHnehd6Lv7RVwHYZoa6FqaDgIjLCP7wY7D',
             'PfrxEm07YmMmNZPuwDx2mlGfJuBe8czHQM4GnTJ4PNkuP3zQjLOa780GOdOwvnTrRozN7QDksXWFSmGyJ6GejfIwg2j1jBqEeFqa',
             'h0K9vlEuIQjvhq4wfEruQKatM87fJoxCuIoXkhjvsjdPTXSoiDRULiuAlfMwMXZ4KCiqxaAhnW7VhN4sMoVMttaeDIpRKuU7dmjZ',
             'Xhezu4ozYmhp9uiBt8paG9l9SpcL3UrnGZKuwY8ZBgTOtczLrFfmNLPgvexDosOaM2fXw2kxf1sN68MBbVy0SrEJ9O8PxlRJk1da',
             'zScLvvaTYnoWah0rZiUh0DCl9vgws7xRQBkI2NOILbFC0s78AsYSzowSihzogCrK7YQGMvtwXKGxPmBWywXuWv70qnhMhRrBqoHE',
             'WhXCyAndVPzvxLFmvu4CeGgfI23yDmgDRs7NhESgHDb9muhdgkolhYFx5bUjz1t1KloXxwZdXUBGv1zSoXNgj65Yko7EZWsWbk3t',
             'r22Rp2P2H4CewCl70UL0qlozV5csGuU5ApT8sXGa37o0nBS9o5zYBKvC1zGxM55j1UX6PaAqky8Ap1NzFEoA4wsvTXnENq2ti8HC',
             '7hsPYER6aehJNWQopi9iRAEAmCaBVehEPNBOnsz83g9U7P5f9FbUW3mXKmBtP7Sp8kEreBJ0m7Rv8rWDuH2dwrEkCAs7edPaB6tr',
             'tbpduY1yYgDjcQyKzZFMFjCgzJYQn7PCEoB4l5SBXG3TvlGUafk9hZAxjhqCCtZ3tZmvTXGCD5G1IReg0ZMhFe22JXY4qwjVp3Sz',
             'Pnwh7VPxhVQu4uXHTyzbmKtYYTCWMB6o97Xc9weiodzCuQSwmOw0ps7rKaDxhZXNTP5QqrvXjZj7ggvf1IdfCIHg1Liu3TlBO2nL',
             'bSiHGMqJv2Ltud2ugjJAQP3wjB6pxiGd8SyYkKDwAdesEHcmKpzj3qsUkoqaYG3PdD7oeVtPomcGtYMmm1zqFZIDKzXoskJWcN5b',
             'w2BHVK5yNBm9KZo9JoYJld3RFxaF5cpvwJsyD8TLbFTij8FVfDBPYPubnaOpHsptLYusuEKQGhXNWGodkj4CL1nBbQuFf4e5z3eo',
             'lc2OwbkfrdO1ov6fCSLe2tBjjU3XOcMnbkEQzD7PMQoOUIvDOjL62eJAe0lrGy4W98eeCvk8mpZ0kCcKXnK6ofpFr4Dlb2btCSOU',
             'GchyA8FSblUjIAdvWqbaYzxDG1bxgiq0iQhB73SADnQjNByFtudaNmDUKEZel7D7yrAUfiMgxCT2YMPjiuNhe5hPKADeKaKr1K5u',
             'hDsNuFub9igzY6TuqC9cCB7WMtuvnJfkcBK6Re9ON4IHjN4u6lC37PGAoEFaZHiqf2NMmnxFHsN92bJlRoTlHPcMuymUT2RAL9H9',
             'KwgJHijR3QFUlaRzvf2cSxbHUU6l4GomAQqWz13fGWuBXjnhgD4igjdQU4iPGXDSD7JA4oLtMNWo7QIIy6kZtCZvdIEH4GtYMsUg',
             '0OBylG85TFGxIRhbk0Sjehb6xz96uuShQPrQe5va8E9wwuJlewJx9YBOhWQwbdhT0HZ3ehB1rEVQOfR0EJvqu45bH15Pi11DPl7T',
             'zuVaXMTQ0s3NOZfSaRateKKlWkd4uc3gzmYwOMXR1u2c3457Tmwgv9e9b2MhRyGffpY8QIFDtGWhlAeK8PLsGl8jcLNErohGfkJ8',
             'ysUxdjR6xelHlVc1pXqhV3FKnbelCLFUXazcBE0CHggJcjFT9Vpk1m8B7WKrBVOlP2MFpWXHAZf6R9HviSrQPgJfkRjcRJINZEMg',
             'wUMqtM8AQGDzXWwJ7SPgqMxDIADQX9gvZRWihDeOrh7bRJDG2anCmTSP34oHcaua62KLXoDmLKdU22Vc9rxQyCAHkyAV63nO9Ndy',
             'FwahVfsWqTwQtS0NroMPAfCehW0hn2szrkMEn1ebgIDIFmwaeHsC32BVtA8eW6ogSLFaYVLdJh3PZ7KQf0pr1YEhTonUaoYnRQ1j',
             'rkYAjexEQbwZs9FGSkmOfJG8zhoaNUCRO0QYSYdaDIDd0Fsnap2Sumgl2vYYl40Sg6v6NLnEGBqVllHuBXMHMrn06eqRJQZNe92M',
             'K7x99q8tmkRwn8SV6abvHjotVgNgynA1YNsqYpbc8QYJlnOlc7eLykG7jcYDJz17DuakVVDLQIOK1zWaOMWseYeQFS9xAG1AINIE',
             'JiLGtJYin67JV1TWLLAO1qg650N6OACfAzTiuBS2mVH4xrhsvDpRc2N4pw0QBKbc2cQevLyibnQi1YBOxlkf0NdqbT4gt1Wsd0bp',
             'aly6QikmcTlWjg28BFeEvdPAN3xzE0sisd6GivRdnsxWzB77g3RN96MGJHTsulHQkM2PBftfVHYmj57x7zxJaj18ekZ1WraiaZJc',
             'a4ExT9LI9nN5pLRw3hurjpqpyLJ2haycVwgGIMcz4DFRQjUDiUZ3T90aFO5gefeDLkYSs8gMwHnIWuoYLIg0WH4yWAF8dj0VgtjW',
             'FXkY9NeNcLOk6G73mJYAzcerKMSvHquS3mNUb9PglnVNYCeINue2ngx5ObRoqOyVRBcJkBdMiyEQ0WZymHAIW8ksC0puE9zZGSh1',
             'sKhw5hoUxraQ9OPb7ZEd7U42FpB1ckGXMfbVc7ezYBZixkyENsgtRdnoq1bPyhyITF5yM3cpnlxO9bpfaVV6vpJRzhIoeMUKJWnN',
             'tQ9Ac1KKcS7fuzaXVlde4l3KDjHaNUqrXUziJQC6KmRUxt18DN22Z1a31JV5MlZXWlcme3EW5AhRy6Rv3INJ20X34cy8Jx4AbmJp',
             '8wu3wJIb2a7qBCHJnBArLGbIonkIxz20ilIvan3K8oxqv8J4poc1j3ZVU0gAZBGNpwuXVliv75MDczDfcMZX631idc1NsiLaBhu7',
             'U90EMY4rJ7vp2IdSvXqTUoYHnS8TlmeQ3xSmU0ot7mwqOCw2FlCAgCL1teESgnpXKZSDDdETFu3phxUXmMG4K3I8hIjIW2wX6W9j']


async def run_server():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 15555)
    async with server:
        await server.serve_forever()


async def handle_client(reader, writer):
    writer.write(banner().encode('utf-8'))
    await writer.drain()

    response = (await reader.read(1024)).decode('utf8')
    # Lancement du chall
    if response == "start":
        for i in range(5):
            # Choix du QR code
            N_QRcode = random.randint(0,49)
            start = time.time()
            writer.write(send_qrcode(N_QRcode))
            await writer.drain()
            # Vérification de la réponse
            response = (await reader.read(1024)).decode('utf8')
            end = time.time()
            if end - start > 2:
                writer.write("Trop tard !\n".encode('utf8'))
                await writer.drain()
                break
            elif response != DATA_LIST[N_QRcode]:
                writer.write("Mauvaise réponse !\n".encode('utf8'))
                await writer.drain()
                break
            elif i == 4:
                writer.write("Bravo ! Vous avez réussi, voici le flag : FMCTF{U_Ar3_t00_f@$t}\n".encode('utf8'))
                await writer.drain()

    # Erreur de lancement
    else:
        writer.write("Erreur de lancement : fermeture de la connexion\n".encode('utf8'))
        await writer.drain()

    writer.close()
    await writer.wait_closed()
        


def banner():
    """ Show the menu. """
    with open("banner.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text


def send_qrcode(n):
    """ Send QR code to the client. """
    with open(f"qrcode/qrcode{n}.png", "rb") as qrcode_file:
        b64_string = base64.b64encode(qrcode_file.read())
    return b64_string
    
    


if __name__ == "__main__":
    asyncio.run(run_server())
