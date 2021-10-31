def open_or_senior(data):
    arr = []
    for tokens in data:

        if tokens[0] >= 55 and tokens[1] > 7:
            arr.append('Senior')
        else:
            arr.append('Open')
    return arr