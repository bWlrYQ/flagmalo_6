import asyncio, socket, random, base64, time

DATA_LIST = ['Tumzi1zxVWz6nEENz5njgz8U9ddn56QYmao2MHlhIeiFw9XzwWqUnJJz5yZh9FXGpwagZDKykJOA3edIcdMrDAb9RyFgqAM0UoYV',
             'eztkhJyJnD54GIeP4uBO37lw1zrfsIUpJXsXj4BAbLH7F8ko3ti1ChhGHVTNQOqxfkHsEmsfPoUJ3RGrU4mN5N47uRoZ3Z0ArLty',
             'xsVlB7jr2EW31eNVLTCZrNRbva1eBSr0O0TxF8ge97San9oXzAdWb9dHEB0IJrPl9j1jfRdDYTtni7AvfQCeuJkL9Nk1pAxowdRS',
             'TmwnD5nigo0jyZ1S5qeZ39QqByMff4MoTPW1PUkqUVcSHBWjdPTBMQwIZe3PlGUgqmTagTvzi9VkMXJxA1uJgAFE6SpFbVV5pYRE',
             'OpSpCgjCEWmVAmWCgtCMoZdtkDrTFFLs7FfF82xYMOmv4Isq4SxpPGEzmJHOKmt2FpNjIoQecHAeeFwHo6nSYIJk4D6YT0W4R7SN',
             '1DLwEaesa9b6c5ZdSKWf1qBGPZd2pRbTtZoZLwxwsCaZAKhcb920UFOo7mpDBZanv7ZuEqcLZ8I3zSI082xGNrcbIRHvZocAkRk8',
             'cGucKt6sVoK7cuW9aBxoJyP3NHxWwqg0m8Z74A5cDRe6YBIHRA31YGnjRgDyePqLZo6dRO2LwmIMyRfBslAjQ990PIdAVSmlA6DC',
             'l7C3SKJmxI2EjAi6UDhoskEnxLkkWEYju0x6bMEJPfQfBhY3n8OLtrm0gBg7ni9yiP6wnzdeMURSM5dvLYn59XCI87CXoVEfZJxg',
             'Der9lVgbH9JFhPnhJiHF6MUSKkUugDNc88wrtANe3HviSU2xiFLeyh6LuBSli8s5LO2TxDtQ4AXjPRBHkFjwjmnY0FQ01jcxdgnF',
             'ISBlBEJ6A7X0OlLkAdlZr2Nwn8vJKuzf2v3wfQrwCIeBfUw3BoBWpGCGlOJGrDCRXwuZWXyFDuEK8oOpm3AIKqCymxxzY4BRnAHL',
             'NjihMxoy1bW39nNWH4oMNryFzR3EeKaVfxnTkSjR5kTPjDOUs2AJuTHZjpeFi8okIvosR8b7a6VbHeWLfuPHILNYW9PaFaCP4nAM',
             'c0XaECB3V1Qc8A31ypJ9WXIGoPb25wm3iZf7hXGwBwh4orGi6g9Ni9wD9sLfPPRH4liCDS2OYfRp8BC6pcJV0eOG3T8OJZ8nExnJ',
             'WgH4vm0Wx8RVZ1CfDIt1U1CnCFflRrqn41fBAWyoBTBrqhMCDjncFS5AYldpwO5FXsynoMhm193GlQeV8qrMdVPYYwZKULsBzHHy',
             'W0O0jdC1C96xCLwQUcTtZe8GIlHuYIzAMqGJdrsE4dTqWuK0e6VKGNQlLGlevOq2LfKNt6Esr9W4kVJufYc5loEcScLwoAeLr1zS',
             '4jmFp7wUooL1uj7mpKxxSl4HxJBxxcwgMq8xlM2YPfmacIQim09OfSzUBsNB4dzhLbg28l1wKrDJTBxbQvli7yNxMzQGBm1QDXNt',
             'bFDCP6fFpqb6TxpHDVjZfXoCFWC6grjpot0IkRqvDKnDFpMZZmiwFVzLZnLkcPoy5w4pee8sus9y1YeC7kT4jv3EkVmPmR9Re2S3',
             'VPppJdVrlTAfBs8VeyWuzfqSNecREgyTl9gBsMwyXoEF7svPVggKcfPFlvVxKV1xHMTRX0IuQDWaxChS8D555Poet7pvJXvToaoL',
             'E7HK1SRRrGmC78IQWVwMnGeRiO6Pukv1RDHoowM4CyuuAFEgr12rajnda7SMVJyve5azC3Sctj4wml5xwl0nOhxcngJuy02diJpU',
             'lDO7pLi8Pt7hQnavSsrhsX3NayOSJRlQF63n4Tf0lMLMIyvHWcRX4KLjj4Vkg2AailldLvq35ou2hqw2bqg5pI0yEBJt9cPYkvhv',
             'EtqquXCLLALl2qyqMl3SRUmtgQsrGWQ0TglNq3k4IakFbkTZ2vMHQ3XuQPfogcfriwoEeUQIzuZ7cB5sWgPUXpSPhoTzlu9dl6c8',
             'esOyn1t6nTt9NkMPPPVIxperHYVDP8KUN9a47cBhL8zrNJbIYdzhGNiFx2LgA25c0shyJ6xcTh5TKZoTdgwuImQeneWAMmCqQAlO',
             'HAFwYuPf4iIjkDIMqv2FV7FrIs0HCwsqirw1wXXvXane0V34zXMYxpUL18qHYcRwDaKl9BdSDZnm1MWrNlO6njw708X1ZXTtbQhC',
             'QpjPDx5PG52qNSosPxzLnaAX6XJUdXV04E7MGTsSZqg0sCCmv9013dgoQceYwOogBNfpEbZs0v58P1zRFy2k4V8BlvS3zATChXxs',
             '4U9QoUCt2kfRgWZFEDN68u0APOPxqAZEZQUfdXLtCD6CZaM7XFPcz1nMhRjuIhJKni3xVLLSriFJF7EIPSQfAGzhfIyIeyMSAYvC',
             'kEFn13K7HglsehgK1JIayvIEY1EyG5Q1EiUJR6wFBzZTiBnWefU4TVIyYxNR7a9F0WBrb4iv2eRDaX2q4NYKdT4ryn9KLYCd2yD8',
             '429Nh9kvQut7fKI6wP8IRIOHcY4fXiwmd3YrzlSrK8b72tVmxjXnXYagSDKGFDusdozDWsBfRPrkbqgtOFql0ZYxOsCMTVbyP2kP',
             't0CLDkXdGMxGVKSkxv1sbfNIdEdZ3m7BpxUNLPIt5iPp0J3uf99aoF3mOrmBDd4xjIJ6lUXE2zfi8v9pBe20meHxOYTOEFjvsbs1',
             'r7X67PEtD1dxE0dbxtreCOl1VBEuXVbzIztmyXVVIUb2lzwIldLYZya7IAyYs3NNKXyUL2ZjGcHoHlz801FFgcQbH8NtfvCowe9R',
             'd9rcPeFJPyAF3MzFbCxPORQf42Qv2OpsV9lCscMAsDEftoueKdhvGgAkP3GUP4RuFiS8ub8k9J7pF9CaFoIl70VBTI2PvN1T6WfT',
             'CnftKxKgYmayaZC1hjPB5lIwSpqGjhFuNbMUrliBQkYCcKWmrqoNU0dLHBpUGIjacPW3UacJNb0xS6iW8uukTv5gZcut9sQ1qB1u',
             '94reUkRQ8nGAv9lberMelM27NQ8ilc1vZG0xMCwY4DBCDEnOfuVK75YG2wtHVhdLxICdR5oGn5KEyYKesFQyIrcIuPQozByDfmjF',
             'riKothcBaDRuOcezA2DU0b6i5A6iPzWcvb6KOprnyYWVnEAR2lCpdSlRyzMT9HXOhJfWpDdnr4Cx7rU2qwTxjqvIfYI7AcHxu8Yz',
             '54gcbONDFVMdodVduxpUOjl6J7yCiXJdVot4yIHfQZAmEFb3JMGYZ2lqxeriFdxsnnUX9ZggolsF7UsKZLSOcH80SOx9c80u3Rl3',
             'GN47zVvmzH3wM6wrgKymQo3GYKhJj7C1tq0lumrPZ4QjBsK791WmC9Q3TMi61kBUCLFiSF7zdS8oYX7U4tR48ontVCNVzaTfKDIu',
             'CRS4X1HBEnUhL1HJqA2YqKlSuXUtrKG19Dp6mKj3jSaHB0UkowfV3urLbDyVeVLYFwszNLPOnQOsvDPp4GkigzngHUilQvk2wkLM',
             'q14InBJjQFCNeMfRfPOBiYkAxbRC8U0ps6BsCrchN9GFC0OOnJO6RjevPKNDSdfmd3iepCa52HJlpyew5R2hLaTRfVzU6vxpVDV8',
             'wGzlysLysVM644e12nFvNBJn8aA6GkIwWw4yAVaGlNfARFquO9ele9U9ZJw4RG2ycCEoidvZCnKXr777lsZ3KzE5tzDlSc2kvT3R',
             'iqcVOEU0JfPAT7EkgyrIg4pFdksFI3JBYHdpyaTrRwRQonzawJ9hjIooaNL73TvVLZ9kYY8WnfWdt6YSjOH9JomOlqc8qsPXotnf',
             'RJ3OfOVryrYl3f9KH9QB0e0aYiBbtXj7ZCY8Uuwz48DNOcvBRUmJnZHwxljvwjj7LmPvBA0d6Srh4uBOOF8Cz2IabA9bhYnmAQdH',
             'zSEC1A2nMSs0z2m8igwQGxz4mpmZync4wv8T48IY7wtMYwVYv6mSNHJ9RJX0hFI7gpU6oUuB5ifXe2H5BvgMqbAxD22G5oWsW9tq',
             'zSlaQGXjFzrsemAx1dzkwO5qozTjIFf7PYXF4SoVR2FnyfcyS0dLgaeIKJJRvgjvJdMcPVPYzuXlfXDM6wLujQnh1FbyxImdPRcy',
             'Jcp3NxNRpXLRze05Pu1VE4ibgLPfN9M9PnJs4jgXiKggJa3dax3zZOExljWV78i2gzPH2QuEakBeJXFZhwpDGkXfOdJQeIjlD3qd',
             'GStEC1WN98R6TjKsJb0qm7bFbpcy4EP4pfCwpMiDQyE3GSP9s5r7U89dlz1V8A9805np0GrztfYTWfjtCujUtERuxbCu8mJOdjzZ',
             'n2Xe8uAuQwZ7LlfpBSlfYceWk5uxB2ohX955CBu57A4gmEZVOoIC7fhW2ORDcYYIyq2vAfTflpOa8u2D9wFtDYP2xR7nTHYce0B5',
             'DrKZHaSUGhzWbMcJAgIquHaKs5eMomLtKHRSwGLiclB0hYKh7NBFHPBc1d86do1jKi0pzHWDVbE7wKwJsFX8BxmkGb1J7doawlOg',
             'GwKyIuokzFXQtoa3GVEN5ZBehhMj36WidxcjKujQQ6SBXp1Dp8eCwBVGZzGqubIEDhTzB0Vii8fBEJAAh6ifUTBETxM1zmgGzVLe',
             '6QKc22pn580jyBkL0Hb8bZfcmTizcKHf4ApAeYI1jFpFryKY2Nx1JhDJOIAk8jjQ9CBt4VVo0FjgIPHuM7vDjnOJigNI2dy8kTsU',
             'SpEi6MO7t7yeIs0pmnM536HtsmE4iqRy47t1G9EVO9IiIf1ymQNwAfwpkTUDRcvoynhG3cJO2dKVaDolOiWsLcXZeugQEQXFpGvR',
             '1ALkn7HNdapDsProGcZbzziX9oRYQm3hbPlHg9l9x3NTHSkyJ0GYMuCFR4BooW9Zq8Sx7CdHUMRJ43YKOz6aBB984zEqyo0LHC1u',
             'bx0SU0yYzB0OSvucoAUXD9Vxd5KsPT0DE7aYAbtoI6gVtPljGiBK7lCAT1bmyTe1H79QIcA54cpznNCiZsXap6YJLV5DUBVCWjq7']


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
                writer.write("Bravo ! Vous avez réussi, voici le flag : FMCTF{1t'$_N0t_h@rD_3n0Ugh_4_U}\n".encode('utf8'))
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
