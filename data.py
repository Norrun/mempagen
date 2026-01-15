from functools import reduce
from trie import Trie

vowels = ["a", "e", "i", "o", "u"]
vowel_combos = ["ai", "au", "ea", "ee", "ei", "eu", "ie", "oa", "oe", "oi", "oo", "ou", "ow", "oy", "ue", "ui"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
]
double_consonants = ["b","d","f","g","l","m","n","p","r","s","t","z"]

consonants_combo_begin = reduce(lambda x, y: x.add(y),[
"bl","br","cl","cr","dr","dw","fl","fr","gl","gr","gw","pl","pr","qu","sl","sm","sn","sp","st","str","sw","shr","squ","spr","scr","spl",
"thr","tr","tw"
],
Trie())
consonants_combo_mid = reduce(lambda x, y: x.add(y),[#  \/ Temporarly ignoring c and k (for the most part, mainly "sk")
"bl","br","cl","cr","fl","fr","gl","gr","nt","pl","pr","sp","st","str","scr","spl","thr","tr"
], # Should double consonants be handled here or by a separate, but connected system? double consonants can end with a cluster.
Trie())
consonants_combo_end = reduce(lambda x, y: x.add(y),[# thinking about handeling "lv" "lg" "ls" "ng" ngl "n?" "nkl" "ps" "rs", by adding an e at the end in the Trie
"bs","ct","ds","fs","ft","gs","ks","lb","lch","ld","lf","lk","lp","lt","mp","mph","mpt","nch","nd","ngs",
"nk","nks","nt","pt","rb","rd","rk","rks","rl","rld","rm","rn","rp","rt","rth","sk","sp","st","ts","ths"
],
Trie())