import base64

def basic_encryption(secret, substitution_table, key):
    """
    Params:
    -------
    @type secret: string
    @param secret: text to encrypt
    @type substitution_table: string
    @param substitution_table: substitution table for the first encryption
    @type key: string
    @param key: encryption key
    """
    print("Table de substitution :", substitution_table)
    substituted_secret = ""
    
    for letter in secret:
        index = 0; limit_index = substitution_table.index(letter)
        for y in "ADFGVX":
            for x in "ADFGVX":
                substituted_secret += y+x if index == limit_index else ""
                index += 1
    print("Secret substitué :", substituted_secret)
    return enhanced_encryption(substituted_secret, key)


def enhanced_encryption(secret, key):
    """
    Params:
    -------
    @type secret: string
    @param secret: text to encrypt for the 2nd time
    @type key: string
    @param key: encryption key
    """
    encrypted_secret = ""
    for i in range(len(secret)):
        encrypted_secret += hex(ord(secret[i]) ^ ord(key[i]))[2:].zfill(2)
    return base64.b64encode(bytes(encrypted_secret, "utf-8"))


if __name__ == "__main__":
    secret = input(">> Secret : ").replace(" ", "").upper()
    key = input(">> Clé : ").replace(" ", "").upper()
    print("Message chiffré :", basic_encryption(secret, "VAK3G6S1BWCOFY4Z9DLRHMIQX2TE8P5N7U0J", key))
