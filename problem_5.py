## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value = None):
        self.value = value
        self.children = {}
        self.isword = False
        self.visited = False
        return

    def insert(self, char):
        if char in self.children:
            return
        self.children[char] = TrieNode(char)
        return

    def suffixes(self, suffix = list(), node = None):
        '''

        :param suffix:
        :param node:
        :return:
        if self.children:

            node = self.children
            self.visited = True
            suffix = list()
            for x in node:
                node[x].visited = True
                suffix.append(x)
                if node[x].isword:
                    suffix.append(x)
                for y in node[x].children:
                    #if node[x].isword:
                    #    suffix.append(x)
                    if node[x].children[y].isword:
                        suffix.append(y)
                    suffix.append(x)
                    suffix[-1] += y
                    self.suffix_fn(suffix, node[x].children[y])
            suffix1 = set(suffix)
            return suffix1
        else:
            raise ValueError("No contents in Trie.")
            return
        '''
        if self.children:
            node = self.children
            for x in node:
                suffix.append(x)
                if node[x].isword:
                    suffix.append(x)
                self.suffix_fn(suffix, node[x])
            return suffix


    def suffix_fn(self, suffix, node = None):
        '''

        :param suffix:
        :param node:
        :return:
                for x in node.children:
            visit = node.children[x].visited
            if visit == False:
                node.children[x].visited = True
                suffix[-1] += x
                if node.children[x].isword and len(node.children[x].children) > 0:
                    suffix.append(suffix[-1])
                elif node.children[x].isword:
                    return
                self.suffix_fn(suffix, node.children[x])
        return suffix
        '''
        for x in node.children:
            visit = node.children[x].visited
            if visit == False:
                node.children[x].visited = True
                suffix[-1] += x
                if node.children[x].isword and node.children[x].children:
                    suffix.append(suffix[-1])
                elif node.children[x].isword and not node.children[x].children:
                    return self.suffix_fn(suffix, node.children)
                return self.suffix_fn(suffix, node.children[x])
            else:
                continue
        return suffix


    ''' 
    def suffixes(self, suffix = list(), node = None):
        if (node == None) and (not self.children):
            raise ValueError("There's nothing in the Trie.")
            return
        else:
            if node == None:
                if len(self.children) > 1:
                    for x in self.children:
                        suffix.append(x)
                        node = self.children[x]
                        if node.isword:
                            suffix.append(x)
                        if node.children:
                            self.suffixes(suffix, node)
                        else:
                            continue
                else:
                    x = self.children.keys()[0]
                    suffix.append(x)
                    node = self.children.values()[0]
                    if node.isword:
                        suffix.append(x)
                    for x in node.children:
                        suffix[len(suffix) - 1] += x
                        node = node.children[x]
                        if node.isword:
                            suffix.append(x)
                        if node.children:
                            self.suffixes(suffix, node)
                        else:
                            continue
                return suffix
            else:
                for x in node.children:
                    suffix[len(suffix) - 1] += x
                    if node.children[x].isword and node.children[x].children:
                        suffix.append(suffix[len(suffix) - 1])
                    if node.children:
                        node = node.children[x]
                        if node.children:
                            return self.suffixes(suffix, node)
                        else:
                            return
                    else:
                        return suffix
    '''
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = None
        self.visited = False

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
            for x in prefix:
                if current.children[x] is not None:
                    current = current.children[x]
        return current

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

wordList1 = ["cat", "cate", "catty", "cathy", "catelyn", "cathylyn", "catalan",
             "ant", "anthology", "antagonist", "antonym",
             "fun", "function", "factory",
             "trie", "trigger", "trigonometry", "tripod"
             ]

for word in wordList1:
    MyTrie.insert(word)

#wordList2 = [""]
#for word in shot:
#    MyTrie.insert(word)

x = MyTrie.find("ca")
# In[ ]:
y = list()
y = x.suffixes()
print(y)


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

'''
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='ant');

f("tr")'''