def swap_case(s):
    for i in range(len(s)):
        if s[i].islower():
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
    return s
