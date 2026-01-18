from functools import cache
class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.end_symbol] = True
        return self

    def exists(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return "*" in current
    
    def words_with_prefix(self, prefix):
        matches = []
        current = self.root
        for c in prefix:
            if c not in current:
                return []
            current = current[c]
        return self.search_level(current,prefix,matches)
    @cache
    def letters_of_max_lenghth_word(self,seq,length):
        letters = []
        current = self.root
        depth = 0
        # something something depth first search
    
    def letters_of_min_length_word(self,seq,length):
        letters = []
        current = self.root
        depth = 0


        
