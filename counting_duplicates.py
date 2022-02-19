def duplicate_count(text):
    text = [x.lower() for x in text]
    final = []
    for x in range(len(text)):
        if text.count(text[x]) > 1:
            final.append(text[x])
    final = list(set(final))
    return len(final)
