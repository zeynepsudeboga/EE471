"""Media item classes for a simple library system."""


class MediaItem:
    """A generic item in a library that can be checked out and returned.

    Attributes:
        title (str): Title of the item.
        author (str): Author or creator of the item.
        is_available (bool): True if the item can be checked out.
    """

    CHECKOUT_SUCCESS = "Successful checkout"
    CHECKOUT_FAILED = "Already out"

    def __init__(self, title, author, is_available=True):
        """Create a media item, available by default."""
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """Check out the item if it is available.

        Returns:
            str: CHECKOUT_SUCCESS if the item was available,
            otherwise CHECKOUT_FAILED.
        """
        if self.is_available:
            self.is_available = False
            return self.CHECKOUT_SUCCESS
        return self.CHECKOUT_FAILED

    def return_item(self):
        """Mark the item as available again."""
        self.is_available = True

    def __str__(self):
        """Return 'Title by Author [Available/Checked Out]'."""
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    """A book, which also stores its number of pages.

    Attributes:
        page_count (int): Number of pages in the book.
    """

    def __init__(self, title, author, page_count, is_available=True):
        """Create a book with a page count."""
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        """Return the base description followed by the page count."""
        return f"{super().__str__()} - {self.page_count} pages"


class DVD(MediaItem):
    """A DVD, which prints a care reminder on every successful checkout.

    Attributes:
        duration_minutes (int): Running time of the DVD in minutes.
    """

    CARE_REMINDER = "Handle with care: Do not scratch the disc."

    def __init__(self, title, author, duration_minutes, is_available=True):
        """Create a DVD with its running time in minutes."""
        super().__init__(title, author, is_available)
        self.duration_minutes = duration_minutes

    def checkout(self):
        """Check out the DVD and remind the borrower to handle it carefully.

        Returns:
            str: The same result as MediaItem.checkout().
        """
        result = super().checkout()
        # We compare with the constant, not the text itself, so changing the message won't break this.
        if result == self.CHECKOUT_SUCCESS:
            print(self.CARE_REMINDER)
        return result


class LibraryCollection:
    """A container that holds the media items of a library."""

    def __init__(self):
        """Create an empty collection."""
        self.items = []

    def add_item(self, item):
        """Add a MediaItem (or any of its subclasses) to the collection.

        Raises:
            TypeError: If item is not a MediaItem.
        """
        # We block wrong objects here, otherwise list_available() would crash when it looks for is_available.
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem objects can be added.")
        self.items.append(item)

    def list_available(self):
        """Return the titles of all items that are currently available."""
        return [item.title for item in self.items if item.is_available]