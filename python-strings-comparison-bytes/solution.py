def compare_strings(a: str, b: str) -> int:
    """
    Compare `a` and `b` lexicographically by code point, WITHOUT
    using the <, >, or == operators on the whole strings. Use a
    loop over positions with ord() on individual characters.

    Return -1 if a < b, 0 if a == b, 1 if a > b.
    A string that is a proper prefix of another is smaller.
    """
    limit = min(len(a), len(b))

    for i in range(limit):
        char_a = ord(a[i])
        char_b = ord(b[i])

        if char_a < char_b:
            return -1
        if char_a > char_b:
            return 1
            
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
        
    return 0
    
def compare_ignoring_case(a: str, b: str) -> int:
    """
    Same return convention as compare_strings, but the strings
    are compared after applying casefold() to both. You may use
    the built-in comparison operators here.
    """
    a = a.casefold()
    b = b.casefold()

    if a < b:
        return -1
    if a > b:
        return 1

    return 0

def caesar_shift(s: str, k: int) -> str:
    """
    Shift every ASCII letter in `s` forward by `k` positions in
    the alphabet, wrapping from "z" to "a" (and "Z" to "A").
    Case is preserved. Characters that are not ASCII letters are
    left unchanged. `k` may be negative or larger than 26.
    Use ord(), chr(), and %.

    Example: caesar_shift("Abc, xyz!", 3) -> "Def, abc!"
    """
    result = ""

    for char in s:
        if "a" <= char <= "z":
            shifted = (ord(char) - ord("a") + k ) % 26
            result += chr(ord("a") + shifted)
        elif "A" <= char <= "Z":
            shifted = (ord(char) - ord("A") + k) % 26
            result += chr(ord("A") + shifted)
        else:
            result += char
    return result
    
def utf8_byte_length(s: str) -> int:
    """
    Return the number of bytes needed to store `s` in UTF-8.
    Example: utf8_byte_length("café") -> 5
    """
    return len(s.encode("utf-8"))

def roundtrip(s: str, encoding: str) -> str:
    """
    Encode `s` using `encoding`, then decode the resulting bytes
    using the same encoding, and return the decoded text. Use
    errors="replace" when encoding so characters the encoding
    cannot represent do not cause an error.
    Example: roundtrip("naïve", "utf-8") -> "naïve"
    """
    data = s.encode(encoding, errors="replace")
    result = data.decode(encoding)
    return result

def is_ascii_only(s: str) -> bool:
    """
    Return True if every character of `s` is ASCII. Do this by
    comparing len(s) with the length of the UTF-8 encoded bytes;
    do not loop over characters.
    """
    return len(s) == len(s.encode("utf-8"))

def first_byte_values(s: str, count: int):
    """
    Return a list of the integer values of the first `count`
    bytes of `s` encoded in UTF-8 (fewer if the encoded data is
    shorter than `count`).
    Example: first_byte_values("Aé", 3) -> [65, 195, 169]
    """
    data = s.encode("utf-8")
    return list(data[:count])
