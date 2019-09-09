def translate(phrase):
    VOWELS = "aeiouy"
    result = ""
    i = 0
    length = len(phrase) - 1
    while i <= length:
        item = phrase[i]
        if item in VOWELS:
            if i == length:
                break
            else:
                if phrase[i + 1] == phrase[i]:
                    result += item
                    i += 3
                else:
                    i += 1
        else:
            result += item
            i += 1
    return result

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
