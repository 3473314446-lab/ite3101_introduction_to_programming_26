def censor(text, word):
    word_length = len(word)
    text_length = len(text)
    stars = "*" * word_length
    result = ""
    index = 0

    while index < text_length:
        # 检查当前位置开始的子串是否匹配目标词
        if index + word_length <= text_length and text[index:index+word_length] == word:
            result += stars
            index += word_length  # 跳过整个已匹配的单词
        else:
            result += text[index]
            index += 1
    
    return result

