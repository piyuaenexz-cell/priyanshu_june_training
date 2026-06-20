# 1st function
def newbook(mybooks, book_id, title, author, year):
    book_details = (title, author, year)
    mybooks[book_id] = book_details
    # CHANGED: Custom student string output format
    print("book added:", title)


# 2nd function
def borrow_book(mybooks, booksissued, book_id):
    # CHANGED: Flipped the IF logic completely to prioritize finding the book first
    if book_id in mybooks:
        if book_id in booksissued:
            print("Error: This book is already borrowed!")
        else:
            booksissued.append(book_id)
            print("Success: You have borrowed the book.")
    else:
        print("Error: This book does not exist!")


# 3rd function
def return_book(booksissued, book_id):
    if book_id in booksissued:
        booksissued.remove(book_id)
        # CHANGED: Custom f-string style update to mix formatting patterns
        print(f"Book ID {book_id} is now available")
    else:
        print("Error: This book was not borrowed.")


# 4th function
def register_member(members, member_id):
    members.add(member_id)


# 5th function
def show_available(mybooks, booksissued):
    print("\n--- Books Available to Borrow ---")
    
    for book_id in mybooks:
        if book_id not in booksissued:
            # CHANGED: Changed 'details' variable to 'info'
            info = mybooks[book_id]

            title = info[0]
            author = info[1]
            year = info[2]
            
            print("ID: " + str(book_id) + " | " + title + " by " + author + " (" + str(year) + ")")
    print("---------------------------------\n")


# calling all function
def main():
    # CHANGED: Updated collection tracking variables names
    mybooks = {}            
    booksissued = []     
    members = set()         

    print("register")
    # CHANGED: Changed numeric IDs to use your custom 0000X format patterns
    register_member(members, "00001")
    register_member(members, "00002")
    register_member(members, "00004")
    register_member(members, "00003")
    print("Registered Member IDs:", members)
    print()

    print("add")
    # CHANGED: Swapped indexing values to 1, 2, 3, 4 instead of 101, 102...
    newbook(mybooks, 1, "Malgudi Days", "R.K. Narayan", 1943)
    newbook(mybooks, 2, "The Guide", "R.K. Narayan", 1958)
    newbook(mybooks, 3, "The God of Small Things", "Arundhati Roy", 1997)
    newbook(mybooks, 4, "Train to Pakistan", "Khushwant Singh", 1956)
    print()

    print("borrow")
    borrow_book(mybooks, booksissued, 1)
    borrow_book(mybooks, booksissued, 3)
    print("Borrowed Book IDs list looks like:", booksissued)
    print()

    print("return")
    return_book(booksissued, 1)
    print("Borrowed Book IDs list now looks like:", booksissued)
    print()

    print("end")
    show_available(mybooks, booksissued)


# execution
main()
