import json

def load_books_from_json(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()

    books = json.loads(data)
    return books 

def search_books_by_author(books, author_name):
    results = []
    for book in books:
        if book["author"].lower() == author_name.lower():
            results.append(book)
    return results 

def search_book_by_genre(books, genre_name):
    results = []
    for book in books:
        if book["genre"].lower() == genre_name.lower():
            results.append(book)
    return results 

def main():
    books = load_books_from_json("books.json")

    print("=== Welcome to the book store ===")
    print("Press 1 to search books by author")
    print("Press 2 to search book by genre")
    print("Press 3 to exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        author = input("Enter author's name: ")
        results = search_books_by_author(books, author)

        if len(results) == 0:
            print("No books found by this author")

        else:
            print("\nBooks by",author + ":")
            for book in results:
                print(f"- {book['title']} {book['genre']}")

    elif choice == "2":
        genre = input("Enter genre name:")
        results = search_book_by_genre(books, genre)

        if len(results) == 0:
            print("No books foud in this genre")

        else:
            print("\nBooks in",genre + ":")
            for book in results:
                print(f"- {book['title']} {book['author']}")

    elif choice == "3":
        print("Thank you for using the Bookstore CLI.")
    else:
        print("Invalid choice. Please run the program again.")

main()