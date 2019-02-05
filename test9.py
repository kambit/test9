def Main(text):
    result = ''
    length = len(text)
    index = 0
    while index < length:
        current_char = substr(text, index, 1)
        result = concat(current_char, result)
        index = index + 1
    return result
