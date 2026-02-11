import secrets
import data
import sys


def generate(length):
    word = ""
    check = secrets.randbelow(2)
    completed = 0
   
    while length - completed > 0:
       
        
        if check == 0: # vowel
            addition, count = get_vowel_component(completed,length)
            word += addition
            completed += count
            check = 1
        else: # consonants
            addition, count = get_consonant_component(completed, length)
            word += addition
            completed += count
            check = 0
        #completed += 1


    return word

def get_vowel_component(completed, length):
    if completed > 0 and secrets.randbelow(2) == 1 and length - completed > 3:
        return secrets.choice(data.vowel_combos), 2
    return secrets.choice(data.vowels), 1
            
def get_consonant_component(completed, length):
    
    if length - completed <= 3: #end
        return get_consonant(completed, length, data.consonants_combo_end2, data.consonants_combo_end3)
    elif completed > 0: #middle
        return get_consonant(completed, length, data.consonants_combo_mid2, data.consonants_combo_mid3)
    else: # beginning
        return get_consonant(completed, length, data.consonants_combo_begin2, data.consonants_combo_begin3)

def get_consonant(completed, length, combo2, combo3):
    remaining = length - completed
    rand = secrets.randbelow(min(remaining,3))
    match rand:
        case 0:
            return secrets.choice(data.consonants), 1
        case 1:
            return secrets.choice(combo2),2
        case 2:
            return secrets.choice(combo3),3



def main():
    word = generate(int(sys.argv[1]))
    print(word)


if __name__ == "__main__":
    main()