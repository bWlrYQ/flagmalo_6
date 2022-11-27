import asyncio, socket, random, base64, time

DATA_LIST = ['T6F99F5jywrTqeQwRTb19rwaYx0MpbxX9k5UPTbPjCA7N961gtZ5rLtpTKEmO52PPD854szHfF9lDh8v4WVFtX5Rj6WU8EzPQWta',
             'rxi5qgmVcOMbLgwR6yFTpaVJ5Nip5tU4U19f481K0OcGh434oZoZPN80h6lhQ1x71USUbMds5rzpbQrP37HidgWXWRDauKlpSYh5',
             'JhITi9rqCHX2GSbvgjWmhUd1uafq63Hq12pEuu06Z3c4NyZnw2jGKEgRgreCVraaAkDwV8Vf0gjce2KLTnBUAjyv1mzhBeoZHsmW',
             'IeS4exREMZ1mCEVYJz7ddiqPA9gahIj8FtEbT6W11F6G4xrDbiVTCPJSnwDrn4HuXDLnoKwT8LxUdbYxY9jV1xLUD2VeYORv00Qi',
             'PuOG5Un8xaviGv7nNOkLTD8FP3prO8tn6uD34dj6U7XxH03jzzLfBvtrJQ0jRUyc8hkJDGMrzwkbsa4wDhjvBypKj47PRh1xc9PO',
             'v7vt3vNZtXuSTpipaaQThx4AiWEa0xPilxunLpYFeOmux3yOA6Bvf7hRHW5jZKXMCslUKqvo2P5twjoTioAVn18jJWdr3oudfsYc',
             'chvPitOlHOE29t9BmTzmpsRiT1gZqyw2quhXS2Uy9DLwP1hQlOaMAsi4xieE4zw5w2Ppp8Yl9fLT2fp7pWPGlWxVoXv5BA7kuJqi',
             'v1gguCZE62SqWyR9poiFsqEOFRbXVEM9fxlKVqI2QKF06t28uIxNIoH8QIqRcCK6jJIvJj8zeSU0gw13CUqqSQ9MjelQ8wGqKhwo',
             'gOfGWsdJfd2h39ZW7N9olrkq8o1TfrtICfvtHy7gZ4o4qKyGFoSCG5sz0zey16145QYZrlIJMTNY8QPfdKRJ0jtQIn76nBTyciKC',
             'fiwnxLZv3g58h5BudVFO5xk9ZTUhZUc81u5fQwoAnkfqydjT0lrARQLkLY9NRROKky5CDR56EP4Jf67hu4RcmLV5OJiNxIifyVqo',
             'kGu69A6YhCbcwDCqylC3HzWfCm0X2M0rh8F87iRd7nmhV5Opf1wzOAumrgCBxtM2FwXcYnRwxgbAgye7PODtDtj9kjS8BU4e9tRs',
             'seijCnFE7uXXHsk4FDticuPAW1Smu19gy7IxPurRoIxt0RxGVgzyM1qNTpHSfvzgPOSDcdKYNA0ga1hyJZdq2gXgQwAbgh1sKDLR',
             'bnC2X31K8L58Pe2Db0ntL2EtRx4HiJ6EtZB11at9cY3nTep21SZcbx3Pa8GlYd6aC4BmBA8plfWS172al4Eje8V4FtqztvI0XVCW',
             'D7e4wuQ7gexi46qz5dVmMMSWbfScbQA8Q0E8HqCvbyJaEn0iDYLjzR8bLX89myrE4A4GtND5T33kAhMYMB2Moj1XD87ooVd7VVmp',
             'dAKf67CVy5wFPAciWfKIB7llCLx3PMW7mi6IhNdN3YTpBXm6xfBNE9SxpOSaCOAFgPTMQW3ZKqZI6Mj91JpV3yAiSAMOzmyQI41e',
             '0SwRjQNd0R3juaz4FVlexuNwlI78Iz9DVEdXn3hp5AHG3j9xxrVvNMUG3rl2IfaXej0tUfnqsQkr6zfbUDzurQCSYEJgGboQqcVG',
             'ccpJvzn3tymORpMOtr739KVkSYBXGCZkdPN2EPfvoHaE3P33K34SSkpVbg9z9ZO416MsKm4UYgri0yZQQuyUddtswdLXyNZSDTnR',
             'mNwHBMy11siBxvHBa4uO9ASRJ1vaf6byJmOqB1hNRSlmW85osKoIi1Xa7vxJiY7plXy0mZGme7ZvBujKRcPcrsElfESlZ40R6tOb',
             'wNwV298VBtnHri5KXHBizIhJcurKs2RwpBV426rIBSTtgqcBMD9Y3qlAIXcWBKB4TCO7za5RqTAGGKAeuk5VCPW5zrsZGrJJww7l',
             'HCHme3UvgMuICYucpJfgS7Ye1IHVueURxtF1fF7prf2Mgnm8ELHB1q6dQBlrtByzhY4vKAfKYokqVt6ItLu323mF9WY7fiI5ukgx',
             'VCik0ipqGMTP4VXnp3ZA06EN5EullQhHvSdIGh3D0jmBhiz05ePDEXYoJLya5n96gtxjGebqO2ok0KVPAVszKl9jESVSw5Q21Dgm',
             'UnVChdVDGG2N3Xq47Guz7BydIvalYjyQHqbDZEHFk6Mgnsxic1lAOykLFWZ0CajOIHY8QCP0hi5HU8fwIwQ5cSM02iF4mL9o6ax0',
             'HeOUf53MvPxmjgmGr6U99vqUgA4FTAraWEPcvUA8wmq3uBgLB432oYse3fCevSbSPDGeTPHu7pun1XC6q10Kn5nY0gTFTxpK4fzL',
             '9gxw13PzlymEW6Nc4Dia5eVLS81ylQiViXm9p43RCJdUninZGgaaNep5oHTR4dO2Ndr2UlGEwKMCx1dGoj5sNnk485T1ADC1I51V',
             'mKsb1O3C3BtxcNB1fKqUND775Jr193WIL5isnaBx4uG7Dydj2E2MwPYmHP2Z8Uu6kmrt3Kyk5GpRSjcytUdSs34cS3tQRwK5qBFe',
             'KOMMmB6LCmtKOo7AQCkfpFqXAHqByfZe785xmMwvwzmFfxpXBU1ywCRju4zw8J8Xtg6AupqZHavePfXQFHSZfwuO86HzNPXqHySR',
             'z4pof4IN6TgpaBohTgPg3D0G8Mic4WQYlPNURiwRtymKTbFlq8AsKkOzG4Y7ssVXTOaDO6wGiyMpuPP5Bl6srVHhbDp6m2pB2hR8',
             '4hBWDSH7HBxQU2W0xaJFTQ8ktMheXd4qReKP9doAjaQCWW3F7g6stL83ghdWea4uexzUxT3m5yEtniwKiLzZMH0MFeyApyzqOBOH',
             'vJqKq1cu5At86NlZhVD6dPCBo4uaDPhJzfW9dNdRlJeVdpTLenvYZ0eAbv3T2qjGcsVHxlxTWU4ICYWbAovjjvP9M3c3KR3hnJxU',
             'iPhLWeUB7egQQvQTosJFsTmEoc8Vwn0WzX608cJ4hz8MySKtsXrkN2HzjDTBJn3BgY5POqNLRYSsW5Wuwmj5FRLcmbwRi3AefvXS',
             'F9yRgDY17tATkRw8uyHy1jarbP404wH9G2b7i1ctVp700GNS7IQlyoQ0RmhLxqhIy7orbxToFaKW8miwUOxy1FhtFLZo2H1VeVbh',
             'q45ARHl1vvgpoCRhrZ6wRbg1jgiEkVocsHC2sUEhzeMARjKm7z8I0573irC4LVcruVF2PR8RFiCPOJXmlIq2WRauJEBHzTgScrXd',
             '3eg9Jvyo3QmVSnNBFMvaGuTkwk5EOMJvgKSSVVTJCGplLCk5Kl66kIr4QpKszpaIcqKYeEgixNjf68R2qFdxULHi8b2Cmbz3wDg2',
             'b3CdivX3BEdvltNdkpRzW2IPI1rKyTr4vGmeenRMObIr3HJMYWKjyKLm32eOEfabOY1xNp9ucaO7tlf8MmGloJzBJp1zniBLooDO',
             '8EUVGR7bqQArdUiislZrK6C3r27wIID9nr20XspbFK0x49erBr6pynlyW7YoeMOqKMjymfwA7w3BnOzzdVsVJu9PN7eeSL5si7OA',
             '28lMiOVuzbUM9LWpgbMA3cQjymb6PpOBCaq74QuN163vGz4ZIrPoi6DOqX7XN1eo0RYbIy5vYH7BTJohZXvEnKdpZw49Cglgdm2h',
             'r4kAlOXW1WFiv86UEUnKhmFxroV45PRn8h3SmbXTFQHVWQ8o2RaI66FL483S8zmpd9h2c6gt0REkI6Jxx6ydq6E2RDBOIVbmLI57',
             'hGwxgbXwyXYU54ZyPfJrskA8GdRzo6dUSplfy3DIJrWE5tvaqXU6GA4VHPELhw2EzWsS5FmXez9EFIFCl207BCvbyAgZ4dUs6jAw',
             'yagvijLJX5BguJjQ1s7L2vCH73BnYz2pk4rHhUvtNQfaCG23luc0BQ1jlNixQrqUZVoTRN9sQPBBjArzMDvJ9qL9FvlOTlRTSQYG',
             'o0HUWL8HVGq3UdqplFKxPatZHG2u1D0FTvwfEOoRpB9y94jHZ5StQZ4LSVhthU5Ybn6vrwt2HxzbXS17bmjKbAMdLSw3mnpSd89h',
             'YFt0D9kAASWd8EdnkUZIxwVVtWaoJieoMW8FSkSIpysLW20hm3d2ae7T0gy4JVDCbmXap8YpYoKxSuz8GAJGakH1uObtQBBVajDu',
             'dr2AS5gB56AfLutJcjPpSwTX5N0ZhAkHn9FFAWcpZytlpCP6FArQGr53yLW8qFmchvvgjKYRUAj1zHVZzMXorxnhyFK2Y8JFsFk5',
             'Oq5XQvb5DlCIQ7IZg7Izf480WUO0ueKa7x2cgHEnLciu9U1cwVGL0DNIaPfxQA9Aegtnu1PDfejCtCCnnxuzWgtwSfWK3zhvKPp8',
             'EbpbQKdASQsaqm7mgHYPScWgqvWR3pT44q3FHFRDgnoXUYq7P3cBE0dlZ1DR1DjqFJpsjdd2ClPUQysxr7zXDC39i0p1eHNQfhnx',
             'mJi9odjerkykne5z9OMCFKQAaI28ITRL3hc8v2NX3AXN9o36TQKY6LMh52wsLSjrln82wn7FRtOLRAyXxQcShDOnvOsc2WeaxC1j',
             'kpba87c02vSAuL2eqT5jaH0z8qJyMBXGwA8Plgewf1qIfiroajXXbRFz4zYe2IV2XZh5T7VFlODI9jycVHZYizGQYKjOH6mDl1g7',
             'lBoKwKlCK2p4jRjDep6jQrb9oPu33DjdBZBr6uX4lD8JBARmz10tz5XGVu4xtjXq02WGw6LwcZNXLFQld8VzyV9nFlkVgPdZobsE',
             'zgQNto73MTM5X6jGnFSyX4qyw6vJxVJbURdoR952X1WlWCFpy6OFDYTXVsM1p02b0gqHOuwSEC2waIUWcStRO9KyKYE6GxaCnDeB',
             'Ia2wBU9TE68plPWnyDSfSjvO2wLSmTOuObiurO5lr3jJRq5xzRN1hBG8r0fYIE6lngqRsznDjUW2BYlv1vxk7KqDd1WJ5YdHxGU2',
             'tk0tF1tRCGsfVsQPOs2dI6596fk3GqiPFNs4rgYo5ObjzIXbq5sLqRs8bkktlLg2mr9lDw256JLtsaO4K2zek9ngrzPhqKK8ywvf']


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
                writer.write("Bravo ! Vous avez réussi, voici le flag : FMCTF{QrC0D3_h@s_No_$ecR3t$_4_U}\n".encode('utf8'))
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
