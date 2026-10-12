from custom_classes import MediaItem

book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

print(book)
print(movie)

print(book.checkout())   # Successful checkout
print(book)              # [Checked Out]
print(book.checkout())   # Already out