from book import Book


class BookShop:
    size = int(input("Enter the number of books: "))

    object_list = []

    for i in range(size):
        name = input("Book Name: ")
        authored = input("Authored: ")
        piece = int(input("Piece: "))
        price = int(input("Price: "))

        object = Book(name, authored, piece, price)
        object_list.append(object)

    object_list[0].add_book(5)
    print(f"New book number: {object_list[0].piece}")
    object_list[2].drop_book(2)
    print(f"New book number: {object_list[2].piece}")

    for object in object_list:
        print(object.display())
