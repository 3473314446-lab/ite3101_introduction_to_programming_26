def censor(text, word):
    words = text.split(" ")
    mask = "*" * len(word)
    result = []
    
    for w in words:
        if w == word:
            result.append(mask)
        else:
            result.append(w)
    
    return " ".join(result)
