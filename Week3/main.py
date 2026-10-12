from custom_classes import MediaItem, Book, DVD, LibraryCollection
book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

print(book)
print(movie)

print(book.checkout())   
print(book)              
print(book.checkout())   

print("\n--- DVD ---")
dvd = DVD("Interstellar", "Christopher Nolan", 169)
print(dvd)
print(dvd.checkout())   
print(dvd)
print(dvd.checkout())   

print("\n--- Library ---")
library = LibraryCollection()

dune = Book("Dune", "Frank Herbert", 412)
matrix = DVD("The Matrix", "Wachowski Sisters", 136)
podcast = MediaItem("Tech Talk", "Lex Fridman")

for item in (dune, matrix, podcast):
    library.add_item(item)
    print("Added:", item)

print("Available before:", library.list_available())

dune.checkout()
matrix.checkout()

print("Available after:", library.list_available())