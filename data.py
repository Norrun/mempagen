

vowels = ["a", "e", "i", "o", "u"]
vowel_combos = ["ai", "au", "ea", "ee", "ei", "eu", "ie", "oa", "oe", "oi", "oo", "ou", "ow", "oy", "ue", "ui"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
]
double_consonants = ["b","d","f","g","l","m","n","p","r","s","t","z"]

consonants_combo_begin2 = [
"bl","br","cl","cr","dr","dw","fl","fr","gl","gr","gw","pl","pr","qu","sl","sm","sn","sp","st","sw",
"tr","tw"
]
consonants_combo_begin3 = ["str","shr","squ","spr","scr","spl","thr",] 
consonants_combo_mid2 = [#  \/ Temporarly ignoring c and k (for the most part, mainly "sk")
"bl","br","cl","cr","fl","fr","gl","gr","nt","pl","pr","sp","st",
] # Should double consonants be handled here or by a separate, but connected system? double consonants can end with a cluster.
consonants_combo_mid3 = ["str","scr","spl","thr",] 
consonants_combo_end2 = [# thinking about handeling "lv" "lg" "ls" "ng" ngl "n?" "nkl" "ps" "rs", by adding an e at the end in the Trie
"bs","ct","ds","fs","ft","gs","ks","lb","ld","lf","lk","lp","lt","mp","nd",
"nk","nt","pt","rb","rd","rk","rl","rm","rn","rp","rt","sk","sp","st","ts",
]
consonants_combo_end3 = ["lch","mph","mpt","nch","ngs","nks","rks","rld","rth","ths"] 