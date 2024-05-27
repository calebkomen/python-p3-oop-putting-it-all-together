class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self.pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = pages

        