from functools import reduce
from trie import Trie

consonants_combo_begin = reduce(lambda x, y:x.add(y),[
"bl","br","cl","cr","dr","fl","fr","gl","gr","pl","pr","sl","sm","sn","sp","st","str","shr","spr","scr","spl","thr","tr"
],
Trie())
consonants_combo_mid = reduce(lambda x, y:x.add(y),[#  \/ Temporarly ignoring c and k (for the most part, mainly "sk")
"bl","br","cl","cr","fl","fr","gl","gr","nt","pl","pr","sp","st","str","scr","spl","thr","tr"
], # Should double consonants be handled here or by a separate, but connected system? double consonants can end with a cluster.
Trie())
consonants_combo_end = reduce(lambda x, y:x.add(y),[
"ct","nt","sp","st"
],
Trie())