from functools import reduce
from trie import Trie
#TODO: split up into combo_start combo_mid and combo_end.
consonants_combo = reduce(lambda x, y:x.add(y),[
"bl","br","cl"
],
Trie())