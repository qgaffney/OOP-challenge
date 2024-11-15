#Create Book class
class Book:
    #Provide attributes
    def __init__(self, title, author, genre, pages):
        #Constructor to initialize
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.read = False

    #Define description() method
    def description(self):
        #Return string
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"

    #Define marked_as_read() method
    def marked_as_read(self):
        #Set read to True
        self.read = True
        #Print message
        print(f"{self.title} by {self.author} has been read.")

    def filter_books(books, filter_by, search_term):
        filtered_books = []
        for book in books:
            if search_term.lower() in book[filter_by].lower():
                filtered_books.append(book)
            return filtered_books 

    def display_books(books):
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Pages: {book['pages']}")

    def display_all_books(books_list):
        print("Please choose an option:")


    if __name__ == "__main__":
        books_list = [
            {"title": "Becoming Supernatural: How Common People Are Doing the Uncommon", "author": "Dr. Joe Dispenza", "genre": "Self-Help", "pages": 384, marked_as_read: True},
            {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Psychological Thriller", "pages": 336},
            {"title": "Catch-22", "author": "Joseph Heller", "genre": "Dark Comedy", "pages": 453}
        ]
    
        all_books = "{books_list.title}"

        while True:
            print("\nChoose filter option:")
            print("1. Display All Books")
            print("2. Filter by Genre")
            print("3. Search by Author")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    if 1:
                        choice = display_all_books
                        print(all_books)
                        break
            elif choice == '2':
                search_term = input("Enter genre: ")
                filtered_books = filter_books(books_list, "genre", search_term)
                display_books(filtered_books)
            elif choice == '3':
                search_term = input("Enter author: ")
                filtered_books = filter_books(books_list, "author", search_term)
                display_books(filtered_books)
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
