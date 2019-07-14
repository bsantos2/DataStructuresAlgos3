# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, path = None, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(path, handler)
        return

    def insert(self, path_array, handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        self.handler = handler
        count = 0
        if path_array:
            for word in path_array:
                if not current:
                    current = RouteTrieNode(path_array[0], self.handler)
                    self.root = current
                    current.insert(word, self.handler)
                    current = current.children[word]
                    count += 1
                else:
                    count += 1
                    if count == len(path_array):
                        current.insert(word, self.handler)
                    else:
                        current.insert(word)
                current = current.children[word]
        return

    def find(self, trie_array):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for word in trie_array:
            if word in current.children:
                current = current.children[word]
            else:
                return None
        return current.handler

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler = None, default_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        if "root" in root_handler:
            path = '/'
            handler = 'root handler'
        self.route_trie = RouteTrie(path, handler)
        self.add_handler(path, handler)
        self.default_handler = default_handler
        return

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if handler is None:
            self.handler = self.default_handler
        else:
            self.handler = handler
        self.route_trie.insert(self.split_path(path), handler)
        return

    def lookup(self, path = '/'):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_array = self.split_path(path)
        handler = self.route_trie.find(path_array)
        if not handler:
            return self.default_handler
        return handler

        pass
    def split_path(self, path = '/'):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        if path == '/':
            path_array = list()
        elif path[-1] == '/': #clean up path if it ends with /
            path = path[:len(path) - 1]
            path_array = path.split('/')
            path_array = path_array[1:]
        else:
            path_array = path.split('/')
            path_array = path_array[1:]
        return path_array

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value = None, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.value = value
        self.handler = handler
        return

    def insert(self, node, handler = None):
        # Insert the node as before
        if node in self.children:
            return
        self.children[node] = RouteTrieNode(node, handler)
        return

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/pikachu", "pikachu handler")

#some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/pikachu/"))  # should print 'pikachu handler'
print(router.lookup("/home/pikachu"))  # should print 'pikachu handler'
print(router.lookup("/home/pikachu/squirtle"))  # should print 'not found handler'
