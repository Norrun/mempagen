import secrets
import data


def generate(length):
    word = ""
    check = secrets.randbelow(2)
    completed = 0
    stage = 0
    while length - completed > 0:
        if completed > 0:
            stage = 1
        elif length - completed <= 3:
            stage = 2
        
        if check == 0:
            if completed > 0:
                pass
            word += secrets.choice(data.vowels)

            check = 1
        else:
            word += secrets.choice(data.consonants)
            check = 0
        completed += 1


    return word


            


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()