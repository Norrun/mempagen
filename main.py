import secrets
import data


def generate(length):
    word = ""
    seq = [secrets.randbelow(2)]
    trie_depth = 0
    print(seq[0])
    while length > 0:

        if seq[-1] == 0:
            if len(seq) < 2 or seq[-2] == 0 or length < 2:
                word += secrets.choice(data.vowels)
                length -= 1
            elif secrets.randbelow(2):
                word += secrets.choice(data.vowel_combos)
                length -= 2
        else:
            pass


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()