class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author

        if not self.check_isbn(isbn):
            raise ValueError("Invalid ISBN")

        self.isbn = isbn

    @staticmethod
    def check_isbn(isbn):
        isbn_digits = ''.join(c for c in isbn if c.isdigit())

        if len(isbn_digits) not in {10, 13}:
            return False

        if len(isbn_digits) == 10:
            checksum = sum(int(digit) * weight for digit, weight in zip(isbn_digits, range(10, 0, -1))) % 11
            return checksum == 0

        if len(isbn_digits) == 13:
            checksum = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn_digits[:-1])) % 10
            return (10 - checksum) % 10 == int(isbn_digits[-1])
