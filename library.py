class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self._borrowed_books = []          # protected
    
    def borrow_book(self, book):
        self._borrowed_books.append(book)
        print(f"✅ {self.name} borrowed '{book.title}'")
    
    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            print(f"✅ {self.name} returned '{book.title}'")
        else:
            print("❌ You didn't borrow this book!")
    
    def show_borrowed_books(self):
        if self._borrowed_books:
            print(f"\n{self.name}'s Borrowed Books:")
            for book in self._borrowed_books:
                print(f"   - {book.title}")
        else:
            print(f"{self.name} has no borrowed books.")


class Student(User):
    def __init__(self, user_id, name, course):
        super().__init__(user_id, name)
        self.course = course
        self._max_books = 3
    
    def borrow_book(self, book):
        if len(self._borrowed_books) >= self._max_books:
            print(f"❌ {self.name} reached maximum limit ({self._max_books} books)!")
            return
        super().borrow_book(book)      # Calling parent method


class Teacher(User):
    def __init__(self, user_id, name, subject):
        super().__init__(user_id, name)
        self.subject = subject
        self._max_books = 10


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"📚 Book added: {book.title}")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"👤 User registered: {user.name}")


# ====================== OBJECT CREATION & ACCESSING ======================

if __name__ == "__main__":
    print("=== Library Management System ===\n")
    
    # 1. Create Library Object
    lib = Library()
    
    # 2. Create Book Objects
    book1 = Book("Python Programming", "Guido van Rossum", "PY101")
    book2 = Book("Clean Code", "Robert C. Martin", "CC202")
    book3 = Book("Atomic Habits", "James Clear", "AH303")
    
    # 3. Add books to library
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    
    # 4. Create User Objects (Student and Teacher)
    student1 = Student("S001", "Harshith", "CSE")
    teacher1 = Teacher("T001", "Dr. Sharma", "Mathematics")
    
    # 5. Register users
    lib.register_user(student1)
    lib.register_user(teacher1)
    
    print("\n--- Borrowing Books ---")
    # Student borrowing
    student1.borrow_book(book1)
    student1.borrow_book(book2)
    student1.borrow_book(book3)        # Should show limit message
    
    # Teacher borrowing
    teacher1.borrow_book(book3)
    
    print("\n--- Showing Borrowed Books ---")
    student1.show_borrowed_books()
    teacher1.show_borrowed_books()
    
    print("\n--- Returning Book ---")
    student1.return_book(book1)
    
    print("\n--- After Return ---")
    student1.show_borrowed_books()