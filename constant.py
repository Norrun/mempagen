from functools import reduce
from trie import Trie
#TODO: split up into combo_start combo_mid and combo_end.
consonants_combo_begin = reduce(lambda x, y:x.add(y),[
"bl","br","cl","cr","fl","fr","gl","gr"
],
Trie())
consonants_combo_mid = reduce(lambda x, y:x.add(y),[
"bl","br","cl","cr","fl","fr","gl","gr","nt"
], # Should double consonants be handled here or by a separate, but connected system? double consonants can end with a cluster.
Trie())
consonants_combo_end = reduce(lambda x, y:x.add(y),[
"ct","nt"
],
Trie())