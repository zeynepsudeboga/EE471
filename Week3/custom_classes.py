class MediaItem:
    CHECKOUT_SUCCESS = "Successful checkout"
    CHECKOUT_FAILED = "Already out"

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return self.CHECKOUT_SUCCESS
        return self.CHECKOUT_FAILED

    def return_item(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"
    
class Book(MediaItem):
    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} - {self.page_count} pages"


class DVD(MediaItem):
    CARE_REMINDER = "Handle with care: Do not scratch the disc."

    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration  # dakika

    def checkout(self):
        result = super().checkout()
        if result == self.CHECKOUT_SUCCESS:
            print(self.CARE_REMINDER)
        return result
    

class LibraryCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem objects can be added.")
        self.items.append(item)

    def list_available(self):
        return [item.title for item in self.items if item.is_available]