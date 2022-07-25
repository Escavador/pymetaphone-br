import itertools

from unidecode import unidecode


def make_upper_clean(word: str):
    original_word = word.upper()

    word = unidecode(original_word)

    # O Unidecode tira a Ç que precisamos para o nosso algoritmos
    pos_cedilha = [i for i, letter in enumerate(original_word) if letter == "Ç"]
    for i in pos_cedilha:
        word = word[:i] + "Ç" + word[i + 1 :]

    # Replace Y with I
    word = word.replace("Y", "I")

    # Remove duplicate consecutive characters if is not R or S without regex
    word_pieces = []
    for i, g in itertools.groupby(word):

        if i not in ["R", "S"]:
            word_pieces.append(i)
        else:
            word_pieces.extend(list(g))

    return "".join(word_pieces)


def is_vowel(char):
    return char in ["A", "E", "I", "O", "U"]


def convert_to_metaphone(word):
    if word is None or word == "":
        return word

    original = make_upper_clean(word)

    length = len(original)

    # Iterate each character
    metaphone = []
    last_char = " "
    current = 0
    while current < length:
        current_char = original[current]
        ahead_char = original[current + 1] if current + 1 < length else " "
        ahead2_char = original[current + 2] if current + 2 < length else " "
        last2_char = original[current - 2] if current - 2 >= 0 else " "

        match current_char:
            case "A" | "E" | "I" | "O" | "U":
                if last_char.isspace():
                    metaphone.append(current_char)
            case "L":
                if ahead_char == "H":
                    metaphone.append("1")
                elif is_vowel(ahead_char) or last_char.isspace():
                    metaphone.append("L")
            case "T" | "P":
                if ahead_char == "H":
                    if current_char == "P":
                        metaphone.append("F")
                    else:
                        metaphone.append("T")
                    current += 1
                metaphone.append(current_char)
            case "B" | "D" | "F" | "J" | "K" | "M" | "V":
                metaphone.append(current_char)
            case "G":
                if ahead_char == "H":
                    if not is_vowel(ahead2_char):
                        metaphone.append("G")
                if ahead_char in ["H", "E", "I"]:
                    metaphone.append("J")
                else:
                    metaphone.append("G")
            case "R":
                if last_char.isspace() or ahead_char.isspace():
                    metaphone.append("2")
                elif ahead_char == "R":
                    metaphone.append("2")
                    current += 1
                elif is_vowel(last_char) and is_vowel(ahead_char):
                    metaphone.append("R")
                    current += 1
                else:
                    metaphone.append("R")
            case "Z":
                if ahead_char.isspace():
                    metaphone.append("S")
                else:
                    metaphone.append("Z")
            case "N":
                if ahead_char.isspace():
                    metaphone.append("M")
                elif ahead_char == "H":
                    metaphone.append("3")
                    current += 1
                elif last_char != "N":
                    metaphone.append("N")
            case "S":
                if ahead_char == "S":
                    metaphone.append("S")
                    last_char = ahead_char
                    current += 1
                elif ahead_char == "H":
                    metaphone.append("X")
                    current += 1
                elif is_vowel(last_char) and is_vowel(ahead_char):
                    metaphone.append("Z")
                elif ahead_char == "C":
                    if ahead2_char in ["E", "I"]:
                        metaphone.append("S")
                        current += 2
                    elif ahead2_char in ["A", "O", "U"]:
                        metaphone.append("SK")
                        current += 2
                    elif ahead2_char == "H":
                        metaphone.append("X")
                        current += 2
                    else:
                        metaphone.append("S")
                        current += 1
                else:
                    metaphone.append("S")
            case "X":
                if ahead_char.isspace():
                    metaphone.append("X")
                elif last_char == "E":
                    if is_vowel(ahead_char):
                        if last2_char.isspace():
                            metaphone.append("Z")
                        else:
                            if ahead_char in ["E", "I"]:
                                metaphone.append("X")
                                current += 1
                            else:
                                metaphone.append("KS")
                                current += 1
                    elif ahead_char == "C":
                        metaphone.append("S")
                        current += 1
                    elif ahead_char in ["P", "T"]:
                        metaphone.append("S")
                    else:
                        metaphone.append("KS")
                elif is_vowel(last_char):
                    if last2_char in ["A", "E", "I", "O", "U", "C", "K", "G", "L", "R", "X"]:
                        metaphone.append("X")
                    else:
                        metaphone.append("KS")
                else:
                    metaphone.append("X")
            case "C":
                if ahead_char in ["E", "I"]:
                    metaphone.append("S")
                elif ahead_char == "H":
                    if ahead2_char == "R":
                        metaphone.append("K")
                    else:
                        metaphone.append("X")
                    current += 1
                elif (ahead_char == "Q") or (ahead_char == "K"):
                    pass
                else:
                    metaphone.append("K")
            case "H":
                if last_char.isspace():
                    if is_vowel(ahead_char):
                        metaphone.append(ahead_char)
                        current += 1
            case "Q":
                metaphone.append("K")
            case "W":
                if is_vowel(ahead_char):
                    metaphone.append("V")
            case "Ç":
                metaphone.append("S")

        last_char = current_char
        current += 1
    return "".join(metaphone)


if __name__ == "__main__":
    metaphone = convert_to_metaphone("Cazas Baia")
    print(metaphone)
