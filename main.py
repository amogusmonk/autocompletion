from avl import AVLTree

if __name__ == "__main__":
    tree = AVLTree()
    root = None

    print("Welcome to the Autocomplete System!")
    print("Available Actions:\n1. Insert a word\n2. Search for a word\n3. Autocomplete a word\n4. Exit ")

    while True:
        choice = input("Choose an option: ")
        if choice == "4":
            print("Thanks for using the Autocomplete System.")
            break
        elif choice == "1":
            word = input("Word to insert: ")
            root = tree.insert(root, word)
            print(f"'{word}' has been inserted.")
        elif choice == "2":
            searched_word = input("Word to search: ")
            result = tree.search(root, searched_word)
            if result is not None:
                print(f"{searched_word} has been found.")
            else:
                print(f"{searched_word} has not been found.")
        else:
            prefix = input("Enter a prefix: ")
            collection = tree.autocomplete(root, prefix)
            print(f"Suggestions: {collection}")

        
    