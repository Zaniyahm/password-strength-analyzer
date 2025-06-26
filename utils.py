def leetspeak_variants(word):
    substitutions = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5'],
        't': ['7']
    }
    variants = set()
    for i in range(len(word)):
        char = word[i].lower()
        if char in substitutions:
            for sub in substitutions[char]:
                new_word = word[:i] + sub + word[i+1:]
                variants.add(new_word)
    return variants
