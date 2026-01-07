from functools import reduce
from trie import Trie

consonants_combo_begin = reduce(lambda x, y:x.add(y),[
"bl","br","cl","cr","dr","dw","fl","fr","gl","gr","gw","pl","pr","qu","sl","sm","sn","sp","st","str","sw","shr","squ","spr","scr","spl",
"thr","tr","tw"
],
Trie())
consonants_combo_mid = reduce(lambda x, y:x.add(y),[#  \/ Temporarly ignoring c and k (for the most part, mainly "sk")
"bl","br","cl","cr","fl","fr","gl","gr","nt","pl","pr","sp","st","str","scr","spl","thr","tr"
], # Should double consonants be handled here or by a separate, but connected system? double consonants can end with a cluster.
Trie())
consonants_combo_end = reduce(lambda x, y:x.add(y),[# thinking about handeling "lv" "lg" "ls" "ng" ngl "ns" "nkl", by adding an e at the end in the Trie
"ct","ft","lb","lch","ld","lf","lk","lp","lt","mp","mph","nch","nd","nk","nt","sp","st"
],
Trie())