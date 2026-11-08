def censor(text, word):
    word_len = len(word)
    text_len = len(text)
    mask = "*" * word_len
    result = ""
    i = 0
    
    while i < text_len:
        if i + word_len <= text_len and text[i:i+word_len] == word:
            result += mask
            i += word_len 
        else:
            result += text[i]
            i += 1
    
    return result

