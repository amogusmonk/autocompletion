Avl:

Node class
- Constructor for the node (takes in a word)
AVLTree class
- Search: returns the node if found; returns none otherwise
- Basic AVL tree functions: height, balance factor, rotations, and insertion
- Prefix search: helper for autocomplete; identifies the first node that matches the prefix
- Word collection: helper for autocomplete; returns a list of words (not the node object) that have the prefix
- Autocomplete: calls prefix search, check if it's none, then calls word collection to return list of words with prefix

Main:
- Gives user 4 choices: insert word, search for word, autocomplete a word, or quit
- While loop to run the interface until user quits
