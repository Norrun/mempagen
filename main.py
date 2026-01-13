import secrets
import data


def generate(length):
    word = ""
    seq = [secrets.randbelow(2)]
    trie_depth = 0
    print(seq[0])
    while length > 0:

        if seq[-1] == 0:
            if (len(seq) < 2 or seq[-2] == 0 or length < 2) and secrets.randbelow(2) == 1:
                word += secrets.choice(data.vowels)
                length -= 1
            else:
                word += secrets.choice(data.vowel_combos)
                length -= 2
            seq.append(1)
        else:
            random = secrets.randbelow(3)
            if len(seq) < 2 or seq[-2] == 0 or length < 2:
            


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()