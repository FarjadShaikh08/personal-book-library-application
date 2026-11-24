import tkinter as tk

from library_gui import LibraryWindow


class DemoLibrary:
    """GUI-only placeholder for the library service."""

    def __init__(self):
        pass

    def list_books(self):
        return []

    def search_catalog(self, query):
        return []

    def add_book(self, book_id, status, rating):
        pass

    def update_book(self, book_id, status, rating):
        pass

    def delete_book(self, book_id):
        pass


def main():
    root = tk.Tk()

    library = DemoLibrary()
    LibraryWindow(root, library)

    root.mainloop()


if __name__ == "__main__":
    main()
