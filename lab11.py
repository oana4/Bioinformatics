import string


def analyze_symbols(seq):
    symbols = {
        "letters": set(),
        "digits": set(),
        "whitespace": set(),
        "punctuation": set(),
        "other": set()
    }

    for ch in seq:
        if ch.isalpha():
            symbols["letters"].add(ch)
        elif ch.isdigit():
            symbols["digits"].add(ch)
        elif ch.isspace():
            symbols["whitespace"].add(ch)
        elif ch in string.punctuation:
            symbols["punctuation"].add(ch)
        else:
            symbols["other"].add(ch)


    for category, chars in symbols.items():
        if chars:  # skip empty categories
            print(f"{category}: {sorted(chars)}")

text = "adjkbhhudb5673920@"
analyze_symbols(text)
