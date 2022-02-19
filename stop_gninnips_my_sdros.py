def spin_words(sentence):
    arr = sentence.split(" ")
    final = []
    
    for x in arr:
        if len(x)>=5:
            final.append(x[::-1])
        else:
            final.append(x)
    return ' '.join(final)
