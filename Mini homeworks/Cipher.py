def encryptAtbashCipher(plain_txt: str) :
    for i in range(0, len(plain_txt)) :
        encrypted_txt = encrypted_txt + chr(ord('a') + ord('z') - ord(plain_txt[i]))
    
    return encrypted_txt


def decryptAtbashCipher(plain_txt: str) :
    return encryptAtbashCipher(plain_txt)


def encryptCaesarCipher(plain_txt: str, shift_stize: int):
    return encryptVigenereCipher(plain_txt, [shift_stize])


def decryptCaesarCipher(plain_txt: str, shift_stize: int):
    return encryptCaesarCipher(plain_txt, -shift_stize)


def encryptVigenereCipher(plain_txt: str, shift_size: list) :
    if(shift_size == 0) :
        return plain_txt
     
    dict_encrypt = {
        '.' : ',', ',' : '.',
        '!' : '?', '?' : '!',  
        '0' : '1', '1' : '0',    
        '2' : '3', '3' : '2',    
        '4' : '5', '5' : '4',    
        '6' : '7', '7' : '6',    
        '8' : '9', '9' : '8'
    }
    encrypted_txt = ""

    for index in range(0, len(plain_txt)) :
        if plain_txt[index].islower() :
            encrypted_txt = encrypted_txt + chr(ord('a') + (ord(plain_txt[index]) + shift_size[index % len(shift_size)] - ord('a')) % 26)
        elif plain_txt[index].isupper() :
            encrypted_txt = encrypted_txt + chr(ord('A') + (ord(plain_txt[index]) + shift_size[index % len(shift_size)] - ord('A')) % 26)
        elif dict_encrypt.__contains__(plain_txt[index]) and shift_size[index % len(shift_size)] % 2 == 1 :
            encrypted_txt = encrypted_txt + dict_encrypt[plain_txt[index]]
        else :
            encrypted_txt = encrypted_txt + plain_txt[index]

    return encrypted_txt


def decryptVigenereCipher(plain_txt: str, shift_size: list) :
    new_shift_size = []
    for shift in shift_size :
        new_shift_size.append(-shift)
    return encryptVigenereCipher(plain_txt, new_shift_size )


def encryptSimpleEnigmaCipher(key1, key2, key3, plain_txt: str) :
    encrypted_txt = ""

    for char in plain_txt :
        if char.isupper() :
            encrypted_txt = encrypted_txt + key3[ord(key2[ord(key1[ord(char) - ord('A')]) - ord('a')]) - ord('a')].upper()
        elif char.islower() :
            encrypted_txt = encrypted_txt + key3[ord(key2[ord(key1[ord(char) - ord('a')]) - ord('a')]) - ord('a')]
        else :
            encrypted_txt = encrypted_txt + char

    return encrypted_txt


def decryptSimpleEnigmaCipher(key1: str, key2: str, key3: str, plain_txt: str) :    
    encrypted_txt = ""

    for char in plain_txt :
        if char.isupper() :
            encrypted_txt = encrypted_txt + chr(key1.find(chr(key2.find(chr(key3.find(char.lower()) + ord('a'))) + ord('a'))) + ord('a')).upper()
        elif char.islower() :
            encrypted_txt = encrypted_txt + chr(key1.find(chr(key2.find(chr(key3.find(char) + ord('a'))) + ord('a'))) + ord('a'))
        else :
            encrypted_txt = encrypted_txt + char

    return encrypted_txt