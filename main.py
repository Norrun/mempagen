import secrets
import data


def generate(length):
    word = ""
    check = secrets.randbelow(2)
    stage = 0
    while length > 0:
        if check == 0:
            word += secrets.choice(data.vowels)
            check = 1
        else:
            word += secrets.choice(data.consonants)
            check = 0
        length -= 1


    return word


            


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()