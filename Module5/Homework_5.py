CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATIN_SYMBOLS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t",
                 "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANSLATION_DICT = {}
for cyr_symbol, lat_symbol in zip(CYRILLIC_SYMBOLS, LATIN_SYMBOLS):
    TRANSLATION_DICT[ord(cyr_symbol)] = lat_symbol
    TRANSLATION_DICT[ord(cyr_symbol.upper())] = lat_symbol.upper()


def change_signs(text):
    """Замінює в тексті всі символи окрім латинських літе, цифер та пробілу га знак '_'.
       Повертає змінений текст. """
    for sign in text:
        if not (sign.isdigit() or ord(sign) in range(ord('a'), ord('z') + 1) or ord(sign) in range(ord('A'), ord('Z')+1)
                or sign == " "):
            text = text.replace(sign, "_")
    return text


def normalize(text):
    global TRANSLATION_DICT
    latin_text = text.translate(TRANSLATION_DICT)
    return change_signs(latin_text)


if __name__ == '__main__':
    print(normalize("Привіт9$)#тт, я Віта ^-^"))
