# Define Persian Standard Keyboard Layout
fa = ['و', 'پ', 'د', 'ذ', 'ر', 'ز', 'ط', 'ظ', 'گ', 'ک', 'م', 'ن', 'ت', 'ا', 'ل', 'ب', 'ی', 'س', 'ش', 'چ', 'ج', 'ح', 'خ', 'ه', 'ع', 'غ', 'ف', 'ق', 'ث', 'ص', 'ض', '.', '/', '‍', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', '-', '=', '\\']
# Add Capital Keys
fa += ['>', 'ء', 'ٔ', '‌','ٰ', 'ژ', 'ٓ', 'ك', '"', ':', '«', '»', 'ة', 'آ', 'أ', 'إ', 'ي', 'ئ', 'ؤ', '{', '}', '[', ']', 'ّ', 'َ', 'ِ', 'ُ', 'ً', 'ٍ', 'ٌ', 'ْ', '<', '؟', '÷', '!', '٬', '٫', '﷼', '٪', '×', '،', '*', ')', '(', 'ـ', '+', '|']


# Define English QWERTY Layout
en = [',', 'm', 'n', 'b', 'v', 'c', 'x', 'z', '\'', ';', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', ']', '[', 'p', 'o', 'i', 'u', 'y', 't', 'r', 'e', 'w', 'q', '.', '/', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\\']
# Add Capital Keys
en += ['<', 'M', 'N', 'B', 'V', 'C', 'X', 'Z', '"', ':', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', '}', '{', 'P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', '>', '?', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '|']

# A function for convert english chars to persian
def ToPersian(text):
    output = ''
    for l in text:
        try:
            i = en.index(l)
            output += fa[i]
        except:
            output += l
    return output


# A function for convert persian chars to english
def ToEnglish(text):
    output = ''
    for l in text:
        try:
            i = fa.index(l)
            output += en[i]
        except:
            output += l
    return output


# A function for recognition text language
# (If most characters are in the same language, that language is recognized.)
def CheckLang(text):
    e = 0
    f = 0
    for l in text:
        if l in fa:
            f += 1
        elif l in en:
            e += 1
    if e >= (f + e * 50 / 100):
        return 'en'
    return 'fa'

# Main function
def SwiLan(text):
    lang = CheckLang(text)
    if lang == 'en':
        return ToPersian(text)
    else:
        return ToEnglish(text)