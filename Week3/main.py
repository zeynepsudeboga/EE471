from custom_classes import MediaItem, Book, DVD

book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

print(book)
print(movie)

print(book.checkout())   # Successful checkout
print(book)              # [Checked Out]
print(book.checkout())   # Already out

print("\n--- DVD ---")
dvd = DVD("Interstellar", "Christopher Nolan", 169)
print(dvd)
print(dvd.checkout())   # uyarı + Successful checkout
print(dvd)
print(dvd.checkout())   # Already out (uyarı yok)