import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    small_first = ord("a")
    small_last = ord("z")
    big_first = ord("A")
    big_last = ord("Z")
    english_alb = 26
    while shift >= english_alb:
        shift %= english_alb
    for a in plaintext:
        if small_first <= ord(a) <= small_last:
            if ord(a) + shift > small_last:
                ciphertext += chr(small_first + shift - 1 - (small_last - ord(a)))
            else:
                ciphertext += chr(ord(a) + shift)
        elif big_first <= ord(a) <= big_last:
            if ord(a) + shift > big_last:
                ciphertext += chr(big_first + shift - 1 - (big_last - ord(a)))
            else:
                ciphertext += chr(ord(a) + shift)
        else:
            ciphertext += a
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    small_first = ord("a")
    small_last = ord("z")
    big_first = ord("A")
    big_last = ord("Z")
    english_alb = 26
    while shift >= english_alb:
        shift %= english_alb
    for a in ciphertext:
        if small_first <= ord(a) <= small_last:
            if ord(a) - shift < small_first:
                plaintext += chr(small_last - shift + 1 + (ord(a) - small_first))
            else:
                plaintext += chr(ord(a) - shift)
        elif big_first <= ord(a) <= big_last:
            if ord(a) - shift < big_first:
                plaintext += chr(big_last - shift + 1 + (ord(a) - big_first))
            else:
                plaintext += chr(ord(a) - shift)
        else:
            plaintext += a
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    #
    for z in range(0, 25 + 1):
        plaintext = decrypt_caesar(ciphertext, z)
        if (plaintext in dictionary) == True:
            best_shift = z

    return best_shift
