def get_middle(s):
    if len(s) % 2 == 0:
        s = s[(len(s) // 2 - 1):(len(s) // 2 + 1)]
        return s
    else:
        s = s[len(s) // 2:len(s) // 2 + 1]
        return s