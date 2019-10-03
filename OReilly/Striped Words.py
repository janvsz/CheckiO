VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"

def checkio(text):

    text = text.replace(',', ' ').replace('.', ' ').replace('?', ' ')
    text = text.split(' ')
    words = 0
    for word in text:
        count = 0
        if len(word) <= 1:
            continue
        else:
            for letter in range(len(word) - 1):
                if word[letter + 1] in VOWELS and word[letter] in CONSONANTS:
                    count += 1
                elif word[letter + 1] in CONSONANTS and word[letter] in VOWELS:
                    count += 1

        if count == (len(word) - 1):
            words += 1

    return words



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("My name is ...") == 3, "All words are striped"
    # assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
