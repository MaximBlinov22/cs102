def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    if len(keyword) < len(plaintext):
        updatekey = ""
        updatekey += keyword * (len(plaintext) // len(keyword))
        for i in range(0, len(plaintext) - len(updatekey)):
            updatekey += keyword[i]
    else:
        updatekey = keyword[0 : len(plaintext)]
    i = 0
    for a in plaintext:
        if a == " ":
            updatekey = updatekey[0:i] + " " + updatekey[i + 1 :]
        if ord("A") <= ord(a) <= ord("Z"):
            shift = ord(updatekey[i].upper()) - ord("A")
            while shift >= 26:
                shift %= 26
            if ord(a) + shift > ord("Z"):
                ciphertext += chr(ord("A") + shift - 1 - (ord("Z") - ord(a)))
            else:
                ciphertext += chr(ord(a) + shift)
            i += 1
        elif ord("a") <= ord(a) <= ord("z"):
            if plaintext[i].isupper():
                shift = ord(updatekey[i].upper()) - ord("a")
            else:
                shift = ord(updatekey[i].lower()) - ord("a")
            while shift >= 26:
                shift %= 26
            if ord(a) + shift > ord("z"):
                ciphertext += chr(ord("a") + shift - 1 - (ord("z") - ord(a)))
            else:
                ciphertext += chr(ord(a) + shift)
            i += 1
        else:
            ciphertext += a
            i += 1

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    if len(keyword) < len(ciphertext):
        updatekey = ""
        updatekey += keyword * (len(ciphertext) // len(keyword))
        for i in range(0, len(ciphertext) - len(updatekey)):
            updatekey += keyword[i]
    else:
        updatekey = keyword[0 : len(plaintext)]
    i = 0
    for a in ciphertext:
        if a == " ":
            updatekey = updatekey[0:i] + " " + updatekey[i + 1 :]
        if ord("A") <= ord(a) <= ord("Z"):
            if ciphertext[i].isupper():
                shift = ord(updatekey[i].upper()) - ord("A")
            else:
                shift = ord(updatekey[i].lower()) - ord("A")
            while shift >= 26:
                shift %= 26
            if ord(a) - shift < ord("A"):
                plaintext += chr(ord("Z") - shift + 1 + (ord(a) - ord("A")))
            else:
                plaintext += chr(ord(a) - shift)
            i += 1
        elif ord("a") <= ord(a) <= ord("z"):
            if ciphertext[i].isupper():
                shift = ord(updatekey[i].upper()) - ord("a")
            else:
                shift = ord(updatekey[i].lower()) - ord("a")
            while shift >= 26:
                shift %= 26
            if ord(a) - shift < ord("a"):
                plaintext += chr(ord("z") - shift + 1 + (ord(a) - ord("a")))
            else:
                plaintext += chr(ord(a) - shift)
            i += 1
        else:
            plaintext += a
            i += 1

    return plaintext
