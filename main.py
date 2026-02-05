import secrets
import data


def generate(length):
    word = ""
    seq = [secrets.randbelow(2)]
    trie_depth = 0
    current_trie = {}
    print(seq[0])
    while length > 0:
        pass
        

    return word


            


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()