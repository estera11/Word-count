def word_count(phrase):
    words_dictionary = dict()
    separate_words = phrase.split()
    oneWord = []

    for word in separate_words:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1
            oneWord.append(word)
            
    return  words_dictionary


