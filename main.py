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
        
        if check == 0: # vowel
            if completed > 0 and secrets.randbelow(2) == 1 and length - completed > 3:
                word += secrets.choice(data.vowel_combos)
                completed += 2
            else:
                word += secrets.choice(data.vowels)
                check = 1
                completed += 1
            check = 1
        else: # consonants
            random = secrets.randbelow(3)
            if completed == 0: # beginning
                if random == 1:
                    word += secrets.choice(data.consonants_combo_begin2)
                    completed += 2
                elif random == 2:
                    word += secrets.choice(data.consonants_combo_begin3)
                    completed += 3
            elif completed > 0 and length - completed > 3: # middle
                if random == 1:
                    word += secrets.choice(data.consonants_combo_mid2)
                    completed += 2
                elif random == 2:
                    word += secrets.choice(data.consonants_combo_mid3)
                    completed += 3
            elif length - completed <= 3: # end
                if random == 1 or length - completed == 2:
                    word += secrets.choice(data.consonants_combo_end2)
                    completed += 2
                elif random == 2 and length - completed == 3:
                    word += secrets.choice(data.consonants_combo_end3)
                    completed += 3
            else: # default
                word += secrets.choice(data.consonants)
                completed += 1
            check = 0
        #completed += 1


    return word


            


def main():
    word = generate(10)
    print(word)


if __name__ == "__main__":
    main()