from ShiXunCrypto.DualAES import DualAES



def key_generation():
    crypt_obj = DualAES()
    crypt_obj.key_generate()

    with open('PK.pem', 'wb') as f:
        f.write(crypt_obj.pk)
    with open('SK.pem', 'wb') as f:
        f.write(crypt_obj.sk)


def encrypt_demo():
    crypt_obj = DualAES()
    data = 'Hello world!'

    with open('PK.pem', 'rb') as f:
        PK = f.read()
        crypt_obj.import_key(PK)
    
    enc_data = crypt_obj.encrypt(data)
    with open('cipher_text.bin', 'wb') as f:
        f.write(enc_data)


def decrypt_demo():
    crypt_obj = DualAES()
    with open('SK.pem', 'rb') as f:
        SK = f.read()
        crypt_obj.import_key(SK)

    with open('cipher_text.bin', 'rb') as f:
        enc_data = f.read()

    dec_data = crypt_obj.decrypt(enc_data)
    print(dec_data)


if __name__ == '__main__':
    key_generation()
    encrypt_demo()
    decrypt_demo()