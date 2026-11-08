def censor(text, word):
    mask = "*" * len(word)
    return text.replace(word, mask)
