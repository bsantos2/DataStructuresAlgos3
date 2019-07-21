## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value = None):
        self.value = value
        self.children = {}
        self.isword = False
        self.word = None
        return

    def clean_trie(self, node):
        if node:
            for x in node:
                if node[x]:
                    node[x].word = None
                    self.clean_triefn(node[x])
        return

    def clean_triefn(self, node):
        for x in node.children:
            node.children[x].word = None
            self.clean_triefn(node.children[x])
        return

    def insert(self, char):
        if char in self.children:
            return
        self.children[char] = TrieNode(char)
        return

    def suffixes(self, suffix = list()):
        if self.children:
            suffix = list()
            for x in self.children:
                suffix.append(x)
                if self.children[x].isword and self.children[x].children:
                    suffix.append(x)
                self.suffix_fn(suffix, self.children[x])
            self.clean_trie(self.children)
            while True:
                try:
                    suffix.remove('')
                except:
                    return suffix
            return suffix


    def suffix_fn(self, suffix, node = None):
        for x in node.children:
            if len(node.children) > 1:
                if node.word is None:
                    node.word = suffix[-1]
            if node.word is not None and node.children and suffix[-1] != node.word:
                suffix.append(node.word)
            if node.children[x].isword and not node.children[x].children:
                suffix[-1] += x
                suffix.append('')
            elif node.children[x].isword and node.children[x].children:
                suffix[-1] += x
                suffix.append(suffix[-1])
            else:
                suffix[-1] += x
            self.suffix_fn(suffix, node.children[x])
        return suffix



## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self, current_node = None):
        self.root = None

    def insert(self, word):
        current = self.root
        count = 0
        for x in word:
            count += 1
            if current is None:
                current = TrieNode()
                self.root = current
                current.insert(x)
                current = current.children[x]
            else:
                current.insert(x)
                if count == len(word):
                    current.children[x].isword = True
                current = current.children[x]
        return

    def find(self, prefix):
        current = self.root
        if current is None:
            Exception('Cannot find your prefix')
            return
        else:
            try:
                for x in prefix:
                    if current.children[x] is not None:
                        current = current.children[x]
                self.current_node = current
            except:
                print('The word you want does not exist in trie.')
                return None
        return current

MyTrie = Trie()
wordList = ["cat", "cate", "catty", "cathy", "catelyn", "cathylyn", "catalan", "catheter",
             "ant", "anthology", "antagonist", "antonym",
             "fun", "function", "factory",
             "trie", "trigger", "trigonometry", "tripod"
             ]

for word in wordList:
    MyTrie.insert(word)

#from ipywidgets import widgets
#from IPython.display import display
#from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
#interact(f,prefix='ant');

#Example 1: Can't find the suffixes because it does not exist in the first place
print("\nExample 1")
f("x")
#Error is printed

#Example 2: tri
print("\nExample 2")
f("tr")
#Prints: igger, igonometry, ie, ipod

#Example 3: c
print("\nExample 3")
f("c")
#Prints: at, ate, atty, athy, atelyn, athylyn, atalan, atheter

#Example 4: ca
print("\nExample 4")
f("cat")
#Prints: e, ty, hy, elyn, hylyn, alan, heter

#Example 5: cat
print("\nExample 5")
f("ca")
#Prints: t, te, tty, thy, telyn, thylyn, talan, theter

#Example 6: cath
print("\nExample 6")
f("cath")
#Prints: y, ylyn, eter